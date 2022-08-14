from re import A
from hangman_words import word_list

from hangman_art import logo
print(logo)

import random
chosen_word = random.choice(word_list)
blanks = []

end_of_game = False
lives = 6

for i in range(len(chosen_word)):
    blanks += "_"
print(blanks)    

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            blanks[i] = guess
    print(blanks)              

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Game Over!")
            print("The word was ", chosen_word)

    if "_" not in blanks:
        end_of_game = True
        print("Hurray, you won the game!")    
       