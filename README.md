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

- **Docker Desktop:** Necesario para construir y ejecutar los contenedores de la aplicación y la base de datos. Puedes descargarlo desde [Docker Hub](https://www.docker.com/products/docker-desktop/).

## Instalación y Configuración

Sigue estos pasos para poner en marcha el proyecto:

### 1. Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO_AQUI>
cd <NOMBRE_DE_LA_CARPETA_DEL_REPOSITORIO>