import random
import Hangman_Art
import Hangman_word_list
import os
clear = lambda: os.system('cls')


print(Hangman_Art.logo)

for word in Hangman_word_list.word_list:
    chosen_word = random.choice(Hangman_word_list.word_list)

print(chosen_word)

lives = 6

display = []
for letter in range(len(chosen_word)):
    display += "_"
print(display)

end = False
count = 0
while not end:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print("You've already guessed " + guess + ".")

    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter

    print(display)

    if guess not in chosen_word:
        print("You guessed " + guess + ", that's not in the word, you lose a life.")
        print(Hangman_Art.stages[lives])
        lives -= 1
        if lives == -1:
            end = True
            print("You lose!")
            print("The answer is: " + chosen_word)
    if "_" not in display:
        end = True
        print("You Win!")

