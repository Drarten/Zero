import sqlite3 as sq


connection = sq.connect('base.db')
cursor = connection.cursor()

cursor.execute("SELECT count(age) as Возраст FROM Test WHERE day = 1")
connection.commit()












# import sqlite3 as sq


# connection = sq.connect('base.db')
# cursor = connection.cursor()

# cursor.execute("INSERT INTO Test VALUES ('Арсений', '19', '1')")
# connection.commit()