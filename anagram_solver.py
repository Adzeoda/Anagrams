import json
import random

filename='dictionary_data.json'
file= open(filename)
data=json.load(file)

def word_prompt(data, lenght):
    all_words= list(data.key())
    while True:
        word=random.choice(all_words)
        if len(word)< lenght and len (word)>2:
            return word

def shuffle_word(word):
    array = list(word)
    shuffled = word
    while True:
        random.shuffle(array)
        shuffled=''.join(array)
        if shuffled !=word:
            return shuffled

print("welcome to the anagram game!")
while (True):
    ana