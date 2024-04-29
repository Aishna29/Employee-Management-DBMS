from app import db
from model import Employee, Project, ProjectProgress

def upload_initial_data():
    # Add initial employees
    employee1 = Employee(empno='EMP001', firstname='John', lastname='Doe', workdept='IT', phoneno='1234567890')
    employee2 = Employee(empno='EMP002', firstname='Jane', lastname='Smith', workdept='HR', phoneno='9876543210')
    db.session.add(employee1)
    db.session.add(employee2)

    # Add initial projects
    project1 = Project(project_id='PROJ001', project_name='Project A', employee_empno='EMP001')
    project2 = Project(project_id='PROJ002', project_name='Project B', employee_empno='EMP002')
    db.session.add(project1)
    db.session.add(project2)

    # Add initial project progress
    progress1 = ProjectProgress(project_id=1, employee_empno='EMP001', projects_completed=2, projects_remaining=1)
    progress2 = ProjectProgress(project_id=2, employee_empno='EMP002', projects_completed=1, projects_remaining=2)
    db.session.add(progress1)
    db.session.add(progress2)

    db.session.commit()

if __name__ == '__main__':
    db.create_all()
    upload_initial_data()
