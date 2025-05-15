# backend/Dockerfile

# Usar una imagen base oficial de Python.
FROM python:3.11-slim

# Establecer variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# --- INICIO DE COMANDOS DE DIAGNÓSTICO DE RED ---
# Instalar herramientas de red (curl, dnsutils para nslookup, iputils-ping para ping)
# Es posible que la imagen -slim no las tenga.
RUN echo ">>> [DIAGNÓSTICO] Ejecutando apt-get update..." && \
    apt-get update -y && \
    echo ">>> [DIAGNÓSTICO] apt-get update completado. Instalando paquetes..." && \
    apt-get install -y --no-install-recommends curl dnsutils iputils-ping && \
    echo ">>> [DIAGNÓSTICO] Paquetes de diagnóstico instalados."

RUN echo ">>> [DIAGNÓSTICO] Intentando ping a pypi.org..."
RUN ping -c 4 pypi.org || echo ">>> [DIAGNÓSTICO] Ping a pypi.org falló o no está disponible"

RUN echo ">>> [DIAGNÓSTICO] Intentando resolver pypi.org con nslookup..."
RUN nslookup pypi.org || echo ">>> [DIAGNÓSTICO] nslookup pypi.org falló"

RUN echo ">>> [DIAGNÓSTICO] Intentando descargar encabezados de pypi.org con curl..."
RUN curl -Iv https://pypi.org || echo ">>> [DIAGNÓSTICO] Curl a pypi.org falló"
# --- FIN DE COMANDOS DE DIAGNÓSTICO DE RED ---

# --- INICIO DE INSTALACIÓN DE DEPENDENCIAS DEL SISTEMA ---
# Instalar dependencias necesarias para compilar mysqlclient y herramientas de diagnóstico
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        pkg-config \
        default-libmysqlclient-dev \
        # Las siguientes son para los diagnósticos, mantenlas si quieres
        curl \
        dnsutils \
        iputils-ping \
    && rm -rf /var/lib/apt/lists/*
# --- FIN DE INSTALACIÓN DE DEPENDENCIAS DEL SISTEMA ---

# Actualizar pip a la última versión
RUN python -m pip install --upgrade pip

# Copiar el archivo de requerimientos primero para aprovechar el caché de Docker
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código de la aplicación Django al directorio de trabajo /app
COPY . .

# Copiar el script de entrada y darle permisos de ejecución
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Establecer el script de entrada
ENTRYPOINT ["/app/entrypoint.sh"]

# Comando por defecto que se pasará al entrypoint
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]