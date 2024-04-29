# model.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empno = db.Column(db.String(6), nullable=False, unique=True)
    firstname = db.Column(db.String(14), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    workdept = db.Column(db.String(5), nullable=False)
    phoneno = db.Column(db.String(11), nullable=False)
    hireddate = db.Column(db.Date)
    designation = db.Column(db.String(10))
    salary = db.Column(db.Float)
    bonus = db.Column(db.Float)
    birthdate = db.Column(db.Date)
    age = db.Column(db.Integer)
    projects = db.relationship('Project', backref='employee', lazy=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.String(6), nullable=False, unique=True)
    project_name = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    project_description = db.Column(db.String(100))
    employee_empno = db.Column(db.String(6), db.ForeignKey('employee.empno'), nullable=False)
    progress = db.relationship('ProjectProgress', backref='project', lazy=True)

class ProjectProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    employee_empno = db.Column(db.String(6), db.ForeignKey('employee.empno'), nullable=False)
    projects_completed = db.Column(db.Integer, default=0)
    projects_remaining = db.Column(db.Integer, default=0)
