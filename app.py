from flask import Flask, request
import word_by_situation
import situation_word
import Today_Word
import situation_word


app = Flask(__name__)       #웹서버 이름

@app.route('/')             #페이지 주소
def hello():                #페이지에서 띄울 내용
    return '<h5>Hello, World!</h5>' #

    
@app.route('/word_by_situation', methods= ['POST'])
def call_wbs():
    return word_by_situation.wbs()

@app.route('/Today_Word' , methods = ['POST'])
def call_rdw():
    return Today_Word.rdw()

@app.route('/situation_word')

@app.route('/situation_word', methods = ['POST'])
def call_second_branch():
    res = situation_word.second_branch(request.get_json())
    return res







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

