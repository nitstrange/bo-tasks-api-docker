from sqlalchemy import exc
from flask import Blueprint, jsonify, request, render_template

from project.api.models import Task
from project import db

tasks_blueprint = Blueprint('tasks', __name__, template_folder='./templates')


@tasks_blueprint.route('/users/task', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        taskname = request.form['taskname']
        task_description = request.form['task_description']
        db.session.add(Task(taskname=taskname, task_description=task_description))
        db.session.commit()
    tasks = Task.query.all()
    return render_template('task.html', tasks=tasks)


@tasks_blueprint.route('/tasks', methods=['POST'])

def add_task():
    post_data = request.get_json()
    response_object = {
        'status': 'fail',
        'message': 'Invalid payload.',
        'data' : post_data
    }
    #if post_data:
    #    return jsonify(response_object), 400
    taskname = post_data.get('task_name')
    task_description = post_data.get('task_description')
    try:
        task = Task.query.filter_by(taskname=taskname).first()
        if not task:
            db.session.add(Task(taskname=taskname, task_description=task_description))
            db.session.commit()
            response_object['status'] = 'success'
            response_object['message'] = f'{taskname} was added!'
            return jsonify(response_object), 201
        else:
            response_object['message'] = 'Sorry. That email already exists.'
            return jsonify(response_object), 400
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify(response_object), 400


@tasks_blueprint.route('/tasks/<task_id>', methods=['GET'])
def get_single_task(task_id):
    """Get single user details"""
    response_object = {
        'status': 'fail',
        'message': 'Task does not exist'
    }
    try:
        task = Task.query.filter_by(id=int(task_id)).first()
        if not task:
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': {
                    'id': task.id,
                    'task_name': task.task_name,
                    'task_description': task.task_description,
                    'active': "true"
                }
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404


@tasks_blueprint.route('/tasks', methods=['GET'])

def get_all_tasks():
    """Get all tasks"""
    response_object = {
        'status': 'success',
        'data': {
            'tasks': [task.to_json() for task in Task.query.all()]
        }
    }
    return jsonify(response_object), 200

