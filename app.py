from flask import Flask, render_template, request, jsonify
from model import db, Employee, Project, ProjectProgress

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db.init_app(app)
app.app_context().push()

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'GET':
        return render_template('add_employee.html')
    elif request.method == 'POST':
        data = request.form
        new_employee = Employee(
            empno=data['empno'],
            firstname=data['firstname'],
            lastname=data['lastname'],
            midinit=data['midinit'],
            workdept=data['workdept'],
            phoneno=data['phoneno'],
            hireddate=data['hireddate'],
            designation=data['designation'],
            salary=data['salary'],
            bonus=data['bonus'],
            birthdate=data['birthdate'],
            age=data['age']
        )
        db.session.add(new_employee)
        db.session.commit()
        return jsonify(new_employee.serialize()), 201

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([employee.serialize() for employee in employees])

@app.route('/add_project', methods=['POST'])
def add_project():
    data = request.json
    employee_empno = data.get('employee_empno')
    employee = Employee.query.filter_by(empno=employee_empno).first()
    if employee:
        new_project = Project(
            project_id=data['project_id'],
            project_name=data['project_name'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            project_description=data['project_description'],
            employee_empno=employee_empno
        )
        db.session.add(new_project)
        db.session.commit()
        
        project_progress = ProjectProgress.query.filter_by(employee_empno=employee_empno).first()
        if project_progress:
            project_progress.projects_completed += 1
            project_progress.projects_remaining -= 1
        else:
            project_progress = ProjectProgress(
                employee_empno=employee_empno,
                projects_completed=1,
                projects_remaining=0
            )
        db.session.add(project_progress)
        db.session.commit()
        
        return jsonify(new_project.serialize()), 201
    else:
        return jsonify({'error': 'Employee not found!'}), 404

@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.serialize() for project in projects])

@app.route('/project_progress', methods=['GET'])
def get_project_progress():
    project_progress = ProjectProgress.query.all()
    return jsonify([progress.serialize() for progress in project_progress])

@app.route('/project_progress', methods=['POST'])
def create_project_progress():
    data = request.json
    new_progress = ProjectProgress(
        employee_empno=data['employee_empno'],
        projects_completed=data['projects_completed'],
        projects_remaining=data['projects_remaining']
    )
    db.session.add(new_progress)
    db.session.commit()
    return jsonify(new_progress.serialize()), 201

if __name__ == '__main__':
    app.run(debug=True)