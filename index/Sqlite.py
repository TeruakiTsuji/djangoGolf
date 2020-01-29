
import sqlite3

def execute(sql):

	connector = sqlite3.connect('db.sqlite3')
	cursor = connector.cursor()
	cursor.execute(sql)
	ret = cursor.fetchall()
	cursor.close()
	connector.close()

	return ret

