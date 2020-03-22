#import sqlite3
#
#def execute(sql):
#
#	connector = sqlite3.connect('db.sqlite3')
#	cursor = connector.cursor()
#	cursor.execute(sql)
#	ret = cursor.fetchall()
#	cursor.close()
#	connector.close()

#	return ret

import psycopg2

def execute(sql):

	connector = psycopg2.connect(
		host="localhost",
		database="isystemgolf",
		port="5432",
		user="postgres",
		password="root"
	)

	cursor = connector.cursor()
	cursor.execute(sql)
	ret = cursor.fetchall()
	cursor.close()
	connector.close()

	return ret

