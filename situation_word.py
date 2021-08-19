import wordsList

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
        "blockId": "61089b38a5a4854bcb94be97",
      },
      {
        "label": "일상",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "믿음 생활",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97" 
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
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "외롭거나 두려울 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
       {
        "label": "사람이 실망시킬 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
       {
        "label": "다른 사람과 잘 지내고 싶을 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
       {
        "label": "따돌림을 당하는 것 같을 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
       {
        "label": "사람들이 불친절해 보일 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "근심이 있을 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97" 
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
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "괴로움과 위기에 있을 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "일이나 여행으로 집을 떠나있을 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "좁고 이기적인 마음으로 기도 할 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "슬플 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "세상이 하나님보다 위대하게 보일 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "세상이 작아보이고 자신은 커보일 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "아주 좋은 기회가 있을 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "돈이 없을 때 ",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "내가 한 일에 낙심 될 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "의기소침할 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97" 
      }
    ]
    }
    }
    elif req == '믿음 생활':
        res = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": "믿음 생활 속 무슨 일이 있었나요? "
                }
            }
        ],      #블록 생성(선택지)
         "quickReplies": [
      {
        "label": "신앙인으로써 확신이 필요할 때",    #보여질 텍스트
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "죄를 지었을 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "믿음의 발동이 필요할 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "하나님이 멀게 느껴질 때",
        "action": "block",
        "blockId": "61089b38a5a4854bcb94be97"
      },
      {
        "label": "세상이 하나님보다 위대하게 보일 때",
        "action": "block",
        "blockId": "610a1fa1ee2e484fe68aaf8e"
      },
      {
        "label": "열매를 많이 맺고싶을 때",
        "action": "block",
        "blockId": "610a1fa1ee2e484fe68aaf8e"
      }
    ]#두번째 블로 아이디  610a1fa1ee2e484fe68aaf8e
    }
    }   
    return res


def final_word(reqData):
      
  req = str(reqData['userRequest']['utterance'])

  didicoco = ''
  for i in wordsList.words:
    if req in i:
      sum1 = str("\n*** 한 구절만 읽는게 아니라 그 장 전체를 묵상하는 것이 좋아요***\n")
      sum2 = print(i)
      didicoco = sum1 + '\n' + sum2
      break

    res = { 
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text": didicoco
                }
            }
        ]
    }
    }

  return res
