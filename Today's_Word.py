# import random
# import wordsList

# def rdw():
#     random.choice(wordsList.random_words)

# rdw()
import wordsList

def final_word():
    for i in wordsList.words:
        if i.find("슬플 때") != -1: # 위험에 처했을 때 이 부분은 나중에 카톡이랑 연결해서 발화를 넣을 예정
            print("\n*** 한 구절만 읽는게 아니라 그 장 전체를 묵상하는 것이 좋아요***\n")
            print(i)
        else:
            pass
        # if "위험에 처했을 때" in i:
        #     print(i)

final_word()