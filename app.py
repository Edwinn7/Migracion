import mysql.connector
import pandas as pd

# Configuración de la conexión a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="edwin123",
    database="migrada"
)

# Crear un cursor para ejecutar consultas
cursor = db.cursor()

# Cargar datos desde Excel
df = pd.read_excel('C:\\Users\\Nieto\\Documents\\Libro1.xlsm', sheet_name='BaseDeDatosMasGrande')

# Crear la tabla en la base de datos (si aún no existe)
create_table_query = """
CREATE TABLE IF NOT EXISTS Empleado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE,
    departamento VARCHAR(50),
    salario FLOAT
)
"""
cursor.execute(create_table_query)

# Insertar datos en la tabla
for index, row in df.iterrows():
    insert_query = "INSERT INTO Empleado (nombre, apellido, fecha_nacimiento, departamento, salario) VALUES (%s, %s, %s, %s, %s)"
    values = (row['Nombre'], row['Apellido'], row['Fecha de Nacimiento'], row['Departamento'], row['Salario'])
    cursor.execute(insert_query, values)

# Realizar commit y cerrar la conexión
db.commit()
db.close()
