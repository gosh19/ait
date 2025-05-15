# backend/articulos/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action # Importar action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser # Para manejar subida de archivos
from .models import Articulo
from .serializers import ArticuloSerializer
import openpyxl # Para leer archivos Excel

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all().order_by('codigo')
    serializer_class = ArticuloSerializer
    parser_classes = [MultiPartParser] # Añadir MultiPartParser para este ViewSet si la acción lo necesita globalmente
                                      # o especificarlo solo en la acción.

    # Acción personalizada para subir y procesar un archivo Excel
    @action(detail=False, methods=['post'], parser_classes=[MultiPartParser])
    def upload_excel(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file') # 'file' debe ser el nombre del campo en FormData

        if not file_obj:
            return Response({'error': 'No se proporcionó ningún archivo.'}, status=status.HTTP_400_BAD_REQUEST)

        if not file_obj.name.endswith(('.xlsx', '.xls')):
            return Response({'error': 'El archivo debe ser un formato Excel (.xlsx o .xls).'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            workbook = openpyxl.load_workbook(file_obj)
            sheet = workbook.active # Obtener la hoja activa (la primera usualmente)

            # Asumimos que la primera fila son los encabezados: Codigo, Descripcion, Precio
            # Puedes hacer esto más robusto verificando los nombres de los encabezados.
            # header = [cell.value for cell in sheet[1]]
            # print(f"Encabezados detectados: {header}")

            articulos_a_procesar = []
            # Empezar desde la segunda fila para saltar los encabezados
            for row_idx, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
                # Esperamos Codigo en la primera columna, Descripcion en la segunda, Precio en la tercera
                if len(row) < 3 or row[0] is None or row[1] is None or row[2] is None:
                    # Ignorar filas incompletas o con datos esenciales faltantes
                    print(f"Fila {row_idx} ignorada por datos incompletos: {row}")
                    continue
                
                codigo = str(row[0]).strip()
                descripcion = str(row[1]).strip()
                try:
                    precio = float(row[2])
                except (ValueError, TypeError):
                    print(f"Fila {row_idx} ignorada por precio inválido ('{row[2]}'): {row}")
                    continue

                if not codigo or not descripcion: # Doble chequeo después de strip
                    print(f"Fila {row_idx} ignorada por código o descripción vacíos después de strip: {row}")
                    continue
                
                articulos_a_procesar.append({
                    'codigo': codigo,
                    'descripcion': descripcion,
                    'precio': precio
                })

            if not articulos_a_procesar:
                return Response({'mensaje': 'No se encontraron artículos válidos para procesar en el archivo.'}, status=status.HTTP_400_BAD_REQUEST)

            # Procesar los artículos (Crear o Actualizar - Upsert)
            # Esta es una forma simple. Para un mejor rendimiento con muchos datos,
            # se podrían usar bulk_create o bulk_update de Django.
            creados_count = 0
            actualizados_count = 0
            errores = []

            for articulo_data in articulos_a_procesar:
                serializer = self.get_serializer(data=articulo_data)
                # Intentar obtener el artículo existente por código
                articulo_existente = Articulo.objects.filter(codigo=articulo_data['codigo']).first()

                if articulo_existente:
                    # Si existe, actualizarlo (pasamos la instancia al serializer)
                    serializer = self.get_serializer(articulo_existente, data=articulo_data, partial=True) # partial=True para PATCH
                    if serializer.is_valid():
                        serializer.save()
                        actualizados_count += 1
                    else:
                        errores.append({articulo_data['codigo']: serializer.errors})
                else:
                    # Si no existe, crear uno nuevo
                    if serializer.is_valid():
                        serializer.save()
                        creados_count += 1
                    else:
                        errores.append({articulo_data['codigo']: serializer.errors})
            
            mensaje = f"{creados_count} artículo(s) creado(s), {actualizados_count} artículo(s) actualizado(s)."
            if errores:
                return Response({'mensaje': mensaje, 'errores_validacion': errores}, status=status.HTTP_207_MULTI_STATUS) # Multi-Status para éxito parcial
            
            return Response({'mensaje': mensaje}, status=status.HTTP_201_CREATED if creados_count > 0 or actualizados_count > 0 else status.HTTP_200_OK)

        except Exception as e:
            print(f"Error procesando el archivo Excel: {e}") # Log del error en el servidor
            return Response({'error': f'Error al procesar el archivo Excel: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)