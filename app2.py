from flask import Flask

app = Flask(__name__)       #코드네임 초기화 

@app.route('/')
def hi():
    html = "<h1>minji hi~<h1>"
    return html

app.run(debug = True) 