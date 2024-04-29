# api.py
from flask import Blueprint, jsonify, request
from model import ProjectProgress, db

api = Blueprint('api', __name__)

@api.route('/project_progress', methods=['GET'])
def get_project_progress():
    project_progress = ProjectProgress.query.all()
    return jsonify([progress.__dict__ for progress in project_progress])

@api.route('/project_progress', methods=['POST'])
def create_project_progress():
    data = request.json
    new_progress = ProjectProgress(**data)
    db.session.add(new_progress)
    db.session.commit()
    return jsonify(new_progress.__dict__), 201