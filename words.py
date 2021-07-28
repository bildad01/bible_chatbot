import wordsList

def final_word():
    for i in wordsList.words:
        if i.find("위험에 처했을 때") != -1: # 위험에 처했을 때 이 부분은 나중에 카톡이랑 연결해서 발화를 넣을 예정
            print(i)
        else:
            pass
        # if "위험에 처했을 때" in i:
        #     print(i)

final_word()