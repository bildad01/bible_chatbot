from flask import jsonify, request
# 카카오톡 언어인 제이슨 언어로 바꾸는 과정
def wbs():
    req = request.get_json()
    user_say = req["userRequest"]["utterance"]

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": user_say
                    }
                }
            ]
        }
    }
    return res


