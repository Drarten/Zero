import sqlite3 as sq


connection = sq.connect('base.db')
cursor = connection.cursor()

class Aut:
	cursor.execute("""CREATE TABLE IF NOT EXISTS authorize(
		id INT,
		user_name TEXT,
		token TEXT
		)""")

class Con:
	cursor.execute("""CREATE TABLE IF NOT EXISTS content(
		id INT,
		title TEXT,
		content TEXT
		)""")

connection.close()
#В стандартном дистрибутиве SQLite невозможно установить пароль для базы данных SQLite.