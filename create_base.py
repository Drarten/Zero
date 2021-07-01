import sqlite3 as sq


connection = sq.connect('base.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Test(
	name TEXT,
	age INT,
	day INT
	)""")

connection.close()