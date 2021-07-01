import sqlite3 as sq


connection = sq.connect('base.db')
cursor = connection.cursor()

result = cursor.fetchall()
print(result)