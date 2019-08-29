from flask import Flask, render_template,redirect, url_for, request
from flask_mail import Mail, Message
import sqlite3 as sql

app = Flask(__name__)
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'harshitgupta@gmail.com'
app.config['MAIL_PASSWORD'] = '***************'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/list')
def list():
	con = sql.connect('student.db')
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("select * from Student")   
	rows = cur.fetchall();
	return render_template('index.html',rows = rows)


@app.route('/AddStudent',methods=['GET','POST'])
def AddStudent():
	if request.method == 'GET':
		return render_template('Student.html')
	else:
		try:
			firstName = request.form['firstName']
			lastname = request.form['lastName']
			emailid = request.form['email']
			with sql.connect('student.db') as con:
				cur = con.cursor()
				cur.execute("INSERT INTO Student (FirstName,LastName,Emailid) VALUES (?,?,?)",(firstName,lastname,emailid))
				con.commit()
				sendmail(emailid)
		except:
			con.rollback()  
		finally:
			con.close()
			return redirect(url_for('list'))		
		
@app.route('/UpdateStudent/<id>',methods=['GET','POST'])
def UpdateStudent(id):
	if request.method == 'GET':
		try:
			con = sql.connect('student.db')
			con.row_factory = sql.Row
			cur = con.cursor()
			cur.execute("select * from Student where id = ?", id)   
			row = cur.fetchone(); 
		except:
			con.rollback()
		finally:
			con.close()
			return render_template('UpdateStudent.html',row = row)
	else:
		try:
			ID = request.form['id']
			FirstName = request.form['firstName']
			LastName = request.form['lastName']
			Emailid = request.form['email']
			con = sql.connect('student.db')
			cur = con.cursor()
			cur.execute("UPDATE Student SET FirstName = ?,LastName = ?,Emailid = ? where ID = ?", (FirstName,LastName,Emailid,ID))
			con.commit()
		except:
			con.rollback()
		finally:
			con.close()
			return redirect(url_for('list'))
	
@app.route('/DeleteStudent/<id>',methods=['GET'])
def DeleteStudent(id):
	if request.method == 'GET':
		try:
			con = sql.connect('student.db')
			cur = con.cursor()
			cur.execute("DELETE FROM Student WHERE id = ?",id)
			con.commit()
		except:
			con.rollback()
		finally:
			con.close()
			return redirect(url_for('list'))
		
def sendmail(emailid):
	print('Entered in sendmail function......................')
	msg = Message('Hello', sender = 'harshitgupta323@gmail.com', recipients = [emailid])
	msg.body = "Hello Flask message sent from Flask-Mail"
	msg.html = "<h1>Hello Gourav</h1>"
	mail.send(msg)

		
if __name__ == '__main__':
   app.run(debug = True)