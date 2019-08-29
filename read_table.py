import sqlite3 as sql

conn = sql.connect('student.db')
conn.row_factory = sql.Row
cursor = conn.execute('SELECT * FROM Student')
rows = cursor.fetchall()
"""for row in cursor:
	print(row)
	print(type(row))
	print('Id:',row[0])
	print('First Name:',row[1])
	print('Last Name:',row[2])
	print('Email Id:',row[3])"""
	
for row in rows:
	print(row)
	print(type(row))
	print('Id:',row[0])
	print('First Name:',row[1])
	print('Last Name:',row[2])
	print('Email Id:',row[3])