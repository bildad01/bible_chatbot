from flask.scaffold import F
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class user(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(32), nullable=False)

    #password = db.Column(db.string(128), nullable=False)

    def __init__(self, userid, password):
        self.userid = userid
        self.password = password

class thanks_list(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    thanks = db.Column(db.String(128), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # db.ForeignKey('user.id') 가져온다.
    user = db.relationship("user", backref = "user.id")