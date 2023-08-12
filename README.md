# Migrar Base de datos desde excel a SQL

Este proyecto migrar datos desde un archivo Excel a una base de
datos MySQL utilizando Python y SQLConnector

## Requerimientos

Asegúrate de tener los siguientes componentes instalados:

- Python 3.x
- MySQL

## Instalación

1. Clona este repositorio:
git clone https://github.com/tu-usuario/NombreDeTuProyecto.git

2. Instala las dependencias:

pip install -r requirements.txt

## Uso

1. Configura la conexión a tu base de datos MySQL en `app.py`.
2. Coloca tu archivo Excel en la carpeta `data` (si es necesario).
3. Ejecuta la aplicación:

python app.py

requirements.txt:
mysql-connector-python==8.0.26
pandas==1.3.3
