import sqlite3 as sq


connection = sq.connect('base.db')
cursor = connection.cursor()

cursor.execute("INSERT INTO Test VALUES ('Арсений', '19', '1')")
connection.commit()