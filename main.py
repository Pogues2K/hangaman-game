
import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
from replit import clear

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()
    #This lets the user know that they have already guessed the same letter
    if guess in display:
        print(f"You have already entered {guess}")
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    #Check if user is wrong.
    if guess not in chosen_word:
        #This lets the user know that the letter is not in the chosen_word
        lives -= 1
        print(f"You guessed {guess}, it's not in the word.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
