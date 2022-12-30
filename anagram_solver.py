import json
import random

filename = 'dictionary_compact.json'
file = open(filename)
data = json.load(file)


def word_prompt(data, lenght):
    all_words = list(data.key())
    while True:
        word = random.choice(all_words)
        if len(word) < lenght and len(word) > 2:
            return word


def shuffle_word(word):
    array = list(word)
    shuffled = word
    while True:
        random.shuffle(array)
        shuffled = ''.join(array)
        if shuffled != word:
            return shuffled


print("welcome to the anagram game!")
while (True):
    word=word_prompt(data,5)
    question=shuffle_word(word)
    meaning=data[word]

    question = question.lower()
    worrd = word.lower()

    print("\nSlove:", question)
    print("Hint:", meaning)

    for i in range (5,0,-1):
        print("\nAttempts Left:", i)
        guess=input('Make a guess: ').lower()
        if guess==word:
            print("Correct!")
            break
        if i==1:
            print("\nCorrect answer")

    choice = input("\nContine?[y/n]: ")
    print('-'*50)
    if choice == 'n':
        print("\nThank you for playing")
        break