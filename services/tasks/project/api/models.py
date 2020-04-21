# services/users/project/api/models.py


from sqlalchemy.sql import func

from project import db

class Task(db.Model):

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer,nullable=False)
    taskname = db.Column(db.String(128), nullable=False)
    task_description = db.Column(db.String(128), nullable=False)

    def __init__(self, taskname, task_description):
        self.taskname = taskname
        self.task_description = task_description

    def to_json(self):
        return {
            'id': self.id,
            'user_id' : self.user_id,
            'taskname': self.taskname,
            'task_description': self.task_description,
            'active': self.active
        }

