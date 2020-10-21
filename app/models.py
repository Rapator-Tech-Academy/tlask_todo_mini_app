from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(140))
    body = db.Column(db.Text)
    done = db.Column(db.Boolean)

    def __repr__(self):
        return f"< [{self.id}] Task : {self.header}>"