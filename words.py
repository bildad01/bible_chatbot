import wordsList

# def text():

#     ress = {"version": "2.0",
#     "template": {
#         "outputs": [
#             {
#                 "simpleText": {
#                     "text": "¯\_(ツ)_/¯ 더 자세히 알려줄래요? ¯\_(ツ)_/¯ "
#                 }
#             }
#         ]
#     }
#     return ress

def first_branch():
    
    res = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": "¯\_(ツ)_/¯ 더 자세히 알려줄래요? ¯\_(ツ)_/¯ "
                }
            }
        ],      #블록 생성(선택지)
         "quickReplies": [
      {
        "label": "인간 관계",    #보여질 텍스트
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518",
      },
      {
        "label": "일상",
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518"
      },
      {
        "label": "믿음 생활",
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518" 
      }
    ]
    }
}
    return res

def second_branch(reqData):
    req = str(reqData['userRequest']['utterance'])
    if req == '인간 관계':
        res = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": "인간관계에서 무슨 일이 있었나요? "
                }
            }
        ],      #블록 생성(선택지)
         "quickReplies": [
      {
        "label": "위험에 처했을 때",    #보여질 텍스트
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518",
      },
      {
        "label": "외롭거나 두려울 때",
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518"
      },
       {
        "label": "사람이 실망시킬 때",
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518"
      },
       {
        "label": "다른 사람과 잘 지내고 싶을 때",
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518"
      },
       {
        "label": "따돌림을 당하는 것 같을 때",
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518"
      },
       {
        "label": "사람들이 불친절해 보일 때",
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518"
      },
      {
        "label": "근심이 있을 때",
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518" 
      }
    ]
    }
}
    elif req == '일상':
        res = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": "일상 속 무슨 일이 있었나요? "
                }
            }
        ],      #블록 생성(선택지)
         "quickReplies": [
      {
        "label": "평안과 휴식을 원할 때",    #보여질 텍스트
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518",
      },
      {
        "label": "괴로움과 위기에 있을 때",
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518"
      },
       {
        "label": "일이나 여행으로 집을 떠나있을 때",
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518"
      },
       {
        "label": "좁고 이기적인 마음으로 기도 할 때",
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518"?????????????????
      },
       {
        "label": "따돌림을 당하는 것 같을 때",
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518"
      },
       {
        "label": "사람들이 불친절해 보일 때",
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518"
      },
      {
        "label": "근심이 있을 때",
        "action": "block",
        "blockId": "6108bd473dcccc79addb1518" 
      }
    ]
    }
}
    return res


def final_word():
    a  = input() # 이부분 발화
    for i in wordsList.words:
        if a in i:
            print("\n*** 한 구절만 읽는게 아니라 그 장 전체를 묵상하는 것이 좋아요***\n")
            print(i)

final_word()