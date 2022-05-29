import json, requests
words = list(json.loads(requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json').text).keys())

def check_letters(word_letter_list,conundrum_list):
    letter_checks = []
    for l in word_letter_list:
        if (l in conundrum_list) & (word_letter_list.count(l) <= conundrum_list.count(l)):
            letter_checks.append(True)
        else:
            letter_checks.append(False)
    if False not in letter_checks:
        return True
    else:
        return False

def find_solutions(conundrum,num_solutions=1):
    words_list = [[char for char in w] for w in words if len(w)<=len(conundrum)]
    conundrum_list = [char for char in conundrum]
    possible_words = []
    for word in words_list:
        if check_letters(word,conundrum_list) == True:
            possible_words.append(''.join(word))
    solutions = []
    for n in range(0,num_solutions):
        guess = max(possible_words, key=len)
        possible_words.pop(possible_words.index(guess))
        solutions.append(guess)
    return solutions

find_solutions('countdown',100)
