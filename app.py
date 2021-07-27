from flask import Flask
import word_by_situation

app = Flask(__name__)       #웹서버 이름

@app.route('/')             #페이지 주소
def hello():                #페이지에서 띄울 내용
    return '<h5>Hello, World!</h5>' #

@app.route('/test')             #페이지 주소
def hi():                #페이지에서 띄울 내용
    return '<h5>Hello!</h5>' #
    
@app.route('/word_by_situation', methods= ['POST'])
def call_wbs():
    return word_by_situation.wbs()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

