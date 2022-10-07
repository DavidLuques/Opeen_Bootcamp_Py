import sqlite3

conexion=sqlite3.connect("colegio.db")
cursor=conexion.execute("select codigo,nombre,apellido from alumnos")
for fila in cursor:
    print(fila)
conexion.close()