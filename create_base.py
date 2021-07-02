import sqlite3 as sq


connection = sq.connect('base.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS games(
	user_id INT,
	score INT,
	'time' INT
	)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
	rowid INT PRIMARY KEY,
	name TEXT,
	sex INT,
	old INT,
	score INT
	)""")


connection.close()