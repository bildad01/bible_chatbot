from models import user
from flask import request
import random
import wordsList

def rdw():
    req = request.get_json()
    user_say = req["userRequest"]["utterance"]      #사용자 발화 내용

    a = str("싫어")
    if a in user_say:
        ans1 = str(" 이 구절부터 차근차근 시작해봐요! 화이팅!")
        ans2 = random.choice(wordsList.random_words)

        randidumdi = ans1 + "\n" + ans2
    else:
        randidumdi = random.choice(wordsList.random_words)
    #random.sample(wordsList.random_words, 1)

    res = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": randidumdi
                }
            }
        ]
    }
}

    return res
