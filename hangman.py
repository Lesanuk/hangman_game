# Hangman game
from wordslist import words
import random
from rangame import lowest_num

print(lowest_num)

# Dictionary of key:()
hangman_art = {0: ("   ", 
                   "   ", 
                   "   "), 
               1: (" o ", 
                   "   ", 
                   "   "), 
               2: (" o ", 
                   " | ", 
                   "   "), 
               3: (" o ", 
                   "/| ", 
                   "   "), 
               4: (" o ", 
                   "/|\\", 
                   "   "), 
               5: (" o ", 
                   "/|\\ ", 
                   "/  "), 
               6: (" o ", 
                   "/|\\ ", 
                   "/ \\")} # we have to use double slashes but still the output will show a single slash

# for line in hangman_art[6]: # # use [] to access a value by its key
#    print(line)

def display_man(wrong_guesses):
    print("*********")
    for line in hangman_art[wrong_guesses]: # wrong_guesses is used as an index to access a specific value stored at that position in hangman_art
        print(line)
    print("*********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer) # keep in mind
    wrong_guesses = 0
    guessed_letters = set() # we have to add "set" before ()
    is_running = True

    while is_running: # the variable already contains True, so writing True again is unnecessary
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha(): # != means doesnt equal to
            print("invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess # important
        else:
            wrong_guesses += 1 # increases the index used to display the next hangman stage

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running + False


if __name__ == '__main__':
    main()
