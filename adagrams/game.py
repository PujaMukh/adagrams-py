from operator import le
import string
import random
import copy

def draw_letters():
    
    pool_of_letters_dict = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
    string.ascii_letters

    letters_in_hand = []
    counter = 0
    while counter < 10:
        choice =(random.choice(string.ascii_letters))
        choice = choice.capitalize()

        if pool_of_letters_dict[choice] > 0:
            letters_in_hand.append(choice)
            counter+=1
            pool_of_letters_dict[choice]-=1

    # print(letters_in_hand)  
    return letters_in_hand 


#another way to write wave 2
#commenting this code as the other one is smaller

#checks to see if a particular letter is in a list and if
# we get the letter, removes it and returns True
# if we dont get it at the end of the list, return False

# def check_if_letter_in_letter_bank(letter, letter_bank):
#     # letters_copy = copy.deepcopy(letter_bank)

#     for i in range(0, len(letter_bank)):
#         if letter == letter_bank[i]:
#             letter_bank.remove(letter_bank[i])
#             return True
#     return False
# def uses_available_letters(word, letter_bank):
#     for i in range(0, len(word)):
#         if check_if_letter_in_letter_bank(word[i], letter_bank):
#             continue
#         else:
#             return False
#     return True
    
    

def uses_available_letters(word, letter_bank):
    word = word.upper()
    # make copy of letter bank 
    letters_copy = letter_bank.copy()

    for letter in word:
        try:
            letters_copy.remove(letter)
        except ValueError:
            return False
    return True



def score_word(word):
    score_dict = {("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"): 1, 
    ("D", "G"): 2, 
    ("B", "C", "M", "P"): 3, ("F", "H", "V", "W", "Y"): 4,
    ("K"): 5, ("J", "X"): 8, ("Q", "Z"): 10}
    
    score = 0
    for letter in word.upper():
        for item in score_dict.keys():
            if letter in item:
                score += score_dict[item]
    
    if len(word) > 6:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    
    word_score_dict = {}
    max_score = -1
    for word in word_list:
        word_score_dict[word] = score_word(word)
        if score_word(word) > max_score:
            max_score = score_word(word)
    
    winning_word = ()
    min_word_length = 11

    for word, score in word_score_dict.items():
        if score == max_score:
            if len(word) == 10:
                winning_word = (word,score)
                break
            if len(word) < min_word_length:
                min_word_length = len(word)
                winning_word = (word,score) 
    
    return winning_word