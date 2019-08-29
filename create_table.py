import sqlite3

conn = sqlite3.connect('student.db')
print("Opened database successfully")

conn.execute('''
		 CREATE TABLE Student
         (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         FirstName           TEXT    NOT NULL,
         LastName            TEXT    NOT NULL,
         Emailid             TEXT    NOT NULL);
		 ''')
print("Table created successfully")

conn.execute("INSERT INTO Student (FirstName,LastName,Emailid) \
      VALUES ('Harshit','Gupta','harshitgupta323@gmail.com')")

conn.execute("INSERT INTO Student (FirstName,LastName,Emailid) \
      VALUES ('Gourav','Gupta','gouravgupta323@gmail.com')")
	  
conn.execute("INSERT INTO Student (FirstName,LastName,Emailid) \
      VALUES ('Suman','Roy','sumanroy323@gmail.com')")
	  
conn.commit()
print("Records created successfully")
conn.close()