import sqlite3 as sq


connection = sq.connect('base.db')
cursor = connection.cursor()


class table:
	def aut(bool1):
		if bool1:
			cursor.execute("CREATE TABLE IF NOT EXISTS authorize(id INT, user_name TEXT, token TEXT)")

	def con(bool2):
		if bool2:
			cursor.execute("CREATE TABLE IF NOT EXISTS content(id INT, title TEXT, content TEXT)")


table.aut(cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='authorize'"))
table.con(cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='content'"))

connection.close()
#В стандартном дистрибутиве SQLite невозможно установить пароль для базы данных SQLite.
#Прогуглив что-либо про yaml я нихуя не понял

