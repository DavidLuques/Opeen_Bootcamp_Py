import sqlite3
con=sqlite3.connect('name.db')
cursor=con.cursor()

rows=cursor.execute('Select * from users')

for row in rows:
    print(row)


#code here
cursor.close()
con.close()

