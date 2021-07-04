import json

with open('word_list.json') as wl:
        bad_words_list = json.load(wl)


def snitch(words):

    words = words.lower()
    
    user_input_words = words.split(" ")
    
    comparision = set(bad_words_list).intersection(user_input_words)
    return comparision
    # print(wordlist)


# print  (snitch("ass and boobs are bad words "))