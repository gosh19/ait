#!/bin/sh

# Salir inmediatamente si un comando falla
# set -e # Puedes dejarlo comentado por ahora para depurar, o habilitarlo.

# Esperar a la base de datos esté disponible
# Intentamos conectar usando manage.py check hasta que tenga éxito
echo "Esperando a la base de datos..."
while ! python manage.py check --database default > /dev/null 2>&1; do
  echo "Base de datos no disponible, esperando 1 segundo..."
  sleep 1
done
echo "¡Base de datos conectada!"

# Aplicar las migraciones de la base de datos
echo "Aplicando migraciones de la base de datos..."
python manage.py migrate

# Ejecutar el comando pasado al script (lo que esté en CMD del Dockerfile o command de docker-compose)
echo "Iniciando servidor..."
exec "$@" # <--- DESCOMENTA ESTA LÍNEA