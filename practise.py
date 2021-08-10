# from flask import request
# import random
# import wordsList

# def prt():
#     req = request.get_json()
#     user_say = req["userRequest"]["utterance"]      #사용자 발화 내용
    
#     a = str('싫어')
#     if user_say in a:       #user_say 안에 a가 있냐?
#         ans1 = str('이것을 읽어라')
#         ans2 = random.choice(wordsList.random_words)

#         randidumdi = ans1 + '\n' + ans2
#     else:
#         randidumdi = random.choice(wordsList.random_words)

#     res = {
#     "version": "2.0",
#     "template": {
#         "outputs": [
#             {
#                 "simpleText": {
#                     "text": randidumdi          #변수를 이용해 간단하게 원하는 값을 불러들임
#                 }
#             }
#         ]
#     }
# }
#     return res

# prt()

# # print문을 사용하면 안돼는 이유는 나중에 json언어로 다시 바꿔서 줘야하는데 그때 변수명을 하나 입력해야 
#     # 하기 때문에 print보단 변수로 묶어서 사용
#     # a = str('싫아')
#     # if a in user_say :
#     #     print('싫어도 말씀 읽자 ')
#     #     print(random.choice(wordsList.random_words))
    
#     # else:
#     #     print(random.choice(wordsList.random_words))
#     # return



def qnf():
        
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "니노 막시무스 카이로소제 ."
                    }
                }
            ],   
            "quickReplies": [
        {
            "label": "인간 관계",
            "action": "block",
            "blokId": "6108bd473dcccc79addb1518"
        },
        {
            "label": "신앙",
            "action": "block",
            "blokId": "6108bd473dcccc79addb1518"
        },
        ]
        }
    }
    return res


def dfasdf(reqData):
    req = str(reqData['userRequest']['utterance'])
    if req =="인간 관계":
        res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "무슨 일이 있었나욥?."
                    }
                }
            ],   
            "quickReplies": [
        {
            "label": "슬플 때",
            "action": "block",
            "blokId": "6108bd473dcccc79addb1518"
        },
        {
            "label": "친구랑 싸웠을 때",
            "action": "block",
            "blokId": "6108bd473dcccc79addb1518"
        },
        ]
        }
        }
    elif req == "신앙":
        res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "무슨 일이 있었나욥?."
                    }
                }
            ],   
            "quickReplies": [
        {
            "label": "슬플 때",
            "action": "block",
            "blokId": "6108bd473dcccc79addb1518"
        }
        ],
        }
        }
    return res





