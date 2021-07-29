import random
import wordsList

def rdw():
    print(random.choice(wordsList.random_words))
    #random.sample(wordsList.random_words, 1)

rdw()