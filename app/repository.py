from app import db
from app.models import Task

class Repository:

    def create_task(self, entity):
        new_task = Task(
            header=entity.header,
            body=entity.body,
            done=entity.done,
        )
        db.session.add(new_task)
        db.session.commit()
        return new_task
    
    def get_all_tasks(self):
        return Task.query.all()