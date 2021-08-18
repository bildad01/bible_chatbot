from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
#  SQL사용 -> 코드로 데이터를 주고받을수 있는 파일, 관리를 편하게 해줌.

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

    id = db.Column(db.Integer, primary_key=True) # 각 고유한 번호 지정, 그걸로 데이터 추출
    userid = db.Column(db.String(32), nullable=False) # 유저가 주는 아이디, 32비트까지 가능, 띄어쓰기 못하게.
    partners = db.relationship('thanks_list', backref = 'user')  #이 클래스는 'thanks_list'와 연결되어 있다.

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



    
    