from flask import current_app as app
from models import db, migrate, thanks_list
from flask import Flask, request
import word_by_situation
import situation_word
import Today_Word
import Thank_you
import situation_word
import os


app = Flask(__name__)       #웹서버 이름

BASE_DIR = os.path.dirname(__file__)
dbfile = os.path.join(BASE_DIR, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']= True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY']='alskejfmv'

db.init_app(app)
migrate.init_app(app, db, render_as_batch=True)
db.app =app
db.create_all()



@app.route('/')             #페이지 주소
def hello():                #페이지에서 띄울 내용
    return '<h5>Hello, World!</h5>' #

    
@app.route('/word_by_situation', methods= ['POST'])
def call_wbs():
    return word_by_situation.wbs()

@app.route('/Today_Word' , methods = ['POST'])
def call_rdw():
    return Today_Word.rdw()

@app.route('/Thank_you' , methods = ['POST'])
def call_ges():
    return Thank_you.ges()

@app.route('/first_branch', methods = ['POST'])
def call_first_branch():
    return situation_word.res()

@app.route('/second_branch', methods = ['POST'])
def call_second_branch():
    res = situation_word.second_branch(request.get_json())
    return res

@app.route('/final_word', methods = ['POST'])
def call_final_word():
    rew = situation_word.final_word(request.get_json())
    return rew


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

