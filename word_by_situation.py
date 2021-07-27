from flask import jsonify, request

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

