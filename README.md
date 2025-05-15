# Desafío Técnico - Gestor de Artículos

Aplicación web para gestion de "Artículos", permitiendo a los usuarios crear, listar, actualizar, eliminar, importar y exportar artículos mediante archivos Excel.

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Funcionalidades](#funcionalidades)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Pre-requisitos](#pre-requisitos)
- [Instalación y Configuración](#instalación-y-configuración)
  - [1. Clonar el Repositorio](#1-clonar-el-repositorio)
  - [2. Configuración de Variables de Entorno (Opcional)](#2-configuración-de-variables-de-entorno-opcional)
  - [3. Levantar los Servicios con Docker Compose](#3-levantar-los-servicios-con-docker-compose)
- [Uso de la Aplicación](#uso-de-la-aplicación)
  - [Acceso a la Aplicación](#acceso-a-la-aplicación)
  - [Gestión de Artículos (CRUD)](#gestión-de-artículos-crud)
  - [Importar Artículos desde Excel](#importar-artículos-desde-excel)
  - [Descargar Artículos a Excel](#descargar-artículos-a-excel)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Decisiones de Diseño y Suposiciones](#decisiones-de-diseño-y-suposiciones)
- [Posibles Mejoras Futuras](#posibles-mejoras-futuras)

## Descripción del Proyecto

El objetivo es desarrollar una aplicación web para la gestión de artículos. Los artículos deben tener obligatoriamente un código, una descripción y un precio. La aplicación permite realizar operaciones CRUD sobre los artículos y también la importación y exportación de los mismos mediante archivos Excel.

## Funcionalidades

- **CRUD de Artículos:**
  - Crear nuevos artículos.
  - Listar los artículos existentes.
  - Actualizar la información de los artículos.
  - Eliminar artículos.
- **Importación desde Excel:** Permite cargar y/o editar artículos masivamente desde un archivo Excel (`.xlsx` o `.xls`).
- **Exportación a Excel:** Permite descargar la lista completa de artículos en un archivo formato Excel (`.xlsx`).

## Tecnologías Utilizadas

- **Frontend:**
  - ReactJS (v19+)
  - JavaScript (ES6+)
  - HTML5, CSS3
  - `Workspace` API para comunicación con el backend.
  - Librerías: `xlsx`, `file-saver` (para manejo de Excel en el frontend).
- **Backend:**
  - Python (v3.11)
  - Django
  - Django REST Framework (DRF)
  - `openpyxl` (para manejo de Excel en el backend).
  - `mysqlclient` (conector MySQL).
  - `django-cors-headers` (para manejo de CORS).
- **Base de Datos:**
  - MySQL (v8.0)
- **Dockerización:**
  - Docker
  - Docker Compose

## Pre-requisitos

Asegúrate de tener instalados los siguientes programas en tu sistema:

- **Docker Desktop:** 
# Necesario para construir y ejecutar los contenedores de la aplicación y la base de datos. Puedes descargarlo desde [Docker Hub](https://www.docker.com/products/docker-desktop/).

## Instalación y Configuración

# Sigue estos pasos para poner en marcha el proyecto:

### 1. Clonar el Repositorio

```bash
git clone https://github.com/gosh19/ait.git
cd ./ait
```

### 2. Configuración del Backend (Docker)
El backend (Django + MySQL) se ejecuta dentro de contenedores Docker.

a. Navega a la raíz del proyecto (donde se encuentra el archivo docker-compose.yml).

b. Construir y levantar los servicios Docker:
```bash
docker-compose up --build
```
 - El flag --build asegura que las imágenes Docker se construyan la primera vez o si hubo cambios en el Dockerfile o el código del backend.
 - Este comando descargará las imágenes base de Python y MySQL (si no las tienes), construirá la imagen para la aplicación Django, e iniciará los contenedores para el backend y la base de datos.
 - El script entrypoint.sh dentro del contenedor del backend se encargará de:
 - Esperar a que la base de datos MySQL esté lista.
 - Aplicar las migraciones de Django automáticamente para crear las tablas necesarias.
 - Iniciar el servidor de desarrollo de Django.
 - Una vez completado, el backend estará escuchando en http://localhost:8000.

c. Para detener los servicios del backend:
 En la terminal donde ejecutaste docker-compose up, presiona Ctrl+C. O, si lo ejecutaste en segundo plano (con -d), desde la raíz del proyecto ejecuta:

```bash
docker-compose down
```

###  3. Configuración y Ejecución del Frontend (React)
 El frontend de React se ejecuta de forma independiente.

 a. Navega a la carpeta del frontend:
```bash
cd frontend
```

b. Instala las dependencias de Node.js:
Si es la primera vez o si package.json ha cambiado:

```bash
npm install
```
o si usas yarn:bash yarn install

c. Inicia el servidor de desarrollo de React:
```bash
npm start
```
o si usas yarn:bash yarn start
d. Esto abrirá automáticamente la aplicación frontend en tu navegador, usualmente en http://localhost:3000 (para Create React App) o http://localhost:5173 (para Vite). El frontend está configurado para comunicarse con el backend en http://localhost:8000

## Uso de la Aplicación
 Una vez que tanto el backend como el frontend estén en ejecución:

### Acceso a la Aplicación
 Frontend (Interfaz de Usuario): Abre tu navegador y ve a http://localhost:3000 (o el puerto que use tu servidor de desarrollo de React, ej. 5173 si usaste Vite).
 Backend API (Django):
 El endpoint principal para los artículos es http://localhost:8000/api/articulos/. Puedes probarlo con herramientas como Postman o directamente en el navegador.
 La interfaz de administración de Django está en http://localhost:8000/admin/.
 Para acceder al admin, primero necesitas crear un superusuario. Abre una nueva terminal, navega a la raíz del proyecto (ait) y ejecuta:
```bash
docker-compose exec web python manage.py createsuperuser
```
 Sigue las instrucciones para crear tu usuario administrador.
## Gestión de Artículos (CRUD)
 La interfaz de usuario del frontend permite:
 
 Ver la lista de artículos cargados desde la API.\
 Crear un nuevo artículo usando el formulario (botón "Crear Nuevo Artículo"). Los datos se enviarán a la API del backend.\
 Editar un artículo existente (botón "Editar" en cada fila).\
 Eliminar un artículo (botón "Eliminar" en cada fila, con confirmación).\
 Importar Artículos desde Excel\
 Formato del Archivo Excel:\
 El archivo debe ser .xlsx o .xls.\
 La primera fila debe contener los encabezados: Codigo, Descripcion, Precio. (El backend espera estos nombres exactos, sensible a mayúsculas/minúsculas).

### Proceso de Importación:
 En la interfaz del frontend, haz clic en el botón "Importar desde Excel".\
 Selecciona tu archivo Excel.\
 El archivo se enviará al backend para su procesamiento.\
 Adjunto ejemplod e archivo en la raiz del repositorio\
 Se mostrará un mensaje indicando el resultado (artículos creados/actualizados y posibles errores de validación). La lista de artículos en el frontend se actualizará.\
 Descargar Artículos a Excel\
 En la interfaz del frontend, haz clic en el botón "Descargar Excel".\
 Se generará y descargará un archivo articulos.xlsx conteniendo todos los artículos actualmente en la base de datos, con las columnas Codigo, Descripcion y Precio. \
 El archivo es generado por el frontend usando los datos obtenidos de la API.