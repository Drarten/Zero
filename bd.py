import sqlite3 as sq


connection = sq.connect("base.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS test (
	name TEXT,
	age INTEGER,
	dat INTEGER
	)""")

connection.close()