from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate

naming_convention = {
    "ix": "ix_%(column_0_lable)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention = naming_convention))
migrate = Migrate()


class user(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(32), nullable=False)
    partners = db.relationship('thanks_list', backref = 'user')  #

    def __repr__(self):
        return '<user %r>' % self.id

    def __init__(self, userid):
        self.userid = userid

class thanks_list(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    thanks = db.Column(db.String(128), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # db.ForeignKey('user.id') 가져온다.
    
    def __repr__(self):
        return '<thanks_list %r>' % self.id

    def __init__(self, user_id, thanks):
        self.user_id = user_id
        self.thanks = thanks



    
    