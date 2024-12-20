import sqlite3

# Conectar a la base de datos (si no existe, se crea)
conn = sqlite3.connect('mi_base_datos.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla (si ya existe, se omite)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER
    )
''')

# Insertar algunos datos
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 30)")
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Ana', 25)")

# Guardar los cambios
conn.commit()

# Consultar todos los datos
cursor.execute("SELECT * FROM usuarios")
resultados = cursor.fetchall()

# Imprimir los resultados
for fila in resultados:
    print(fila)

# Cerrar la conexión
conn.close()
