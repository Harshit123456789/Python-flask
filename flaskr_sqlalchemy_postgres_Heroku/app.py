from flask import Flask, render_template,redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2

app = Flask(__name__)

if os.environ.get('ENV') == 'production':
	app.config['DEBUG'] = False
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	app.config['SECRET_KEY'] = "Production"
	app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
else:
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:secret@localhost:5432/pythontest'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	app.config['SECRET_KEY'] = "Development"
	app.config['DEBUG'] = True

db = SQLAlchemy(app)

class students(db.Model):

	__tablename__ = 'student'
	
	id = db.Column('id', db.Integer, primary_key = True)
	firstname = db.Column(db.String(100), nullable=False)
	lastname = db.Column(db.String(50), nullable=False)
	email = db.Column(db.String(200), unique=True, nullable=False)

	def __init__(self, firstname, lastname, email):
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
	
	def __repr__(self):
		return "{} {} has Email id {}".format(self.firstname.rstrip(),self.lastname.rstrip(),self.email.rstrip())


@app.route('/list',methods=['GET'])
def list():
	if request.method == 'GET':
		rows = students.query.all()
		return render_template('index.html',rows = rows)
	
	
@app.route('/AddStudent',methods=['GET','POST'])
def Add():
	if request.method == 'POST':
		student = students(request.form['firstName'],request.form['lastName'],request.form['email'])
		db.session.add(student)
		db.session.commit()
		return redirect(url_for('list'))
	else:
		return render_template('Student.html')
	
		
@app.route('/UpdateStudent/<id>',methods=['GET','POST'])
def UpdateStudent(id):
	if request.method == 'POST':
		student = students.query.get(id)
		student.firstname = request.form['firstName']
		student.lastname = request.form['lastName']
		student.email = request.form['email']
		db.session.commit()
		return redirect(url_for('list'))
	else:
		student = students.query.get(id)
		return render_template('UpdateStudent.html',row = student)

	
@app.route('/DeleteStudent/<id>',methods=['GET'])
def DeleteStudent(id):
	if request.method == 'GET':
		student = students.query.get(id)
		db.session.delete(student)
		db.session.commit()
		return redirect(url_for('list'))
		

if __name__ == '__main__':
	app.run()