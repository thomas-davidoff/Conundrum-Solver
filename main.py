import json
import requests

words = list(json.loads(
    requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json').text).keys())


def check_letters(word_letter_list, conundrum_list):
    letter_checks = []
    for letter in word_letter_list:
        if (letter in conundrum_list) & (word_letter_list.count(letter) <= conundrum_list.count(letter)):
            letter_checks.append(True)
        else:
            letter_checks.append(False)
    if False not in letter_checks:
        return True
    else:
        return False


def solve(conundrum, num_solutions=1):
    words_list = [[char for char in w] for w in words if len(w) <= len(conundrum)]
    conundrum_list = [char for char in conundrum]
    possible_words = []
    for word in words_list:
        if check_letters(word, conundrum_list):
            possible_words.append(''.join(word))
    solutions = []
    if len(possible_words) > 0:
        for n in range(0, min(num_solutions, len(possible_words))):
            guess = max(possible_words, key=len)
            possible_words.pop(possible_words.index(guess))
            solutions.append(guess)

    longest = max(solutions, key=len) if len(solutions) > 0 else []
    if len(longest) == len(conundrum):
        print(f'Conundrum has a perfect solution.\nThe solution is {longest}')
    elif len(solutions) == 0:
        print('There is no solution.')
    else:
        print(f"Conundrum doesn't have a perfect solution.\nThe best solution is {longest}")
    return solutions


solve('m', 2)
