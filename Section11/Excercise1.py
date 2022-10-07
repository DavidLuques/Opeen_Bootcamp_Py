import sqlite3

con = sqlite3.connect("colegio.db")

try:
    con.execute("""create table alumnos (
                              codigo integer primary key autoincrement,
                              nombre text,
                              apellido text
                        )""")
    print("se creo la tabla alumnos")
except sqlite3.OperationalError:
    print("La tabla alumnos ya existe")
con.close()

con = sqlite3.connect("colegio.db")
con.execute("insert into alumnos(nombre,apellido) values (?,?)", ("matias", 'alarcon'))
con.execute("insert into alumnos(nombre,apellido) values (?,?)", ("panchi", 'villa'))
con.execute("insert into alumnos(nombre,apellido) values (?,?)", ("peralta", 'perez'))
con.execute("insert into alumnos(nombre,apellido) values (?,?)", ("lara", 'perez'))
con.execute("insert into alumnos(nombre,apellido) values (?,?)", ("pendejo", 'pataki'))
con.execute("insert into alumnos(nombre,apellido) values (?,?)", ("telettubie", 'ritch'))
con.execute("insert into alumnos(nombre,apellido) values (?,?)", ("panchufleto", 'noemi'))

con.commit()
con.close()
# CTRL+ALT+T GENIAL ME DA FUNCIONES PARA WRAPPEAR


