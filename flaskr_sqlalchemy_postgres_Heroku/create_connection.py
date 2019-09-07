import psycopg2

conn = psycopg2.connect(database="pythontest", user = "postgres", password = "secret", host = "127.0.0.1", port = "5432")
print("Opened database successfully")
cur = conn.cursor()
cur.execute('''
	  CREATE TABLE Student
         (ID SERIAL PRIMARY KEY  NOT NULL,
         FirstName           TEXT    NOT NULL,
         LastName            TEXT    NOT NULL,
         Emailid             TEXT    NOT NULL);
	  ''')
print("Table created successfully")
cur.execute("INSERT INTO Student (FirstName,LastName,Emailid) \
      VALUES ('Harshit','Gupta','harshitgupta323@gmail.com')")

cur.execute("INSERT INTO Student (FirstName,LastName,Emailid) \
      VALUES ('Gourav','Gupta','gouravgupta323@gmail.com')")
	  
cur.execute("INSERT INTO Student (FirstName,LastName,Emailid) \
      VALUES ('Suman','Roy','sumanroy323@gmail.com')")
	  
print("Records created successfully")
conn.commit()
conn.close()