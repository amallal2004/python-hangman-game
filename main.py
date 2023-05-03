import os
import random
import hangman_art
import hangman_words

# Set up initial game state
end_of_game = False
word_list = hangman_words.data
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
lives = 6
guessed_letters = []

# Print game logo and testing code
print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')

# Create initial display of underscores to represent unguessed letters
for letter in range(word_length):
    display += '_'
print(display)


# Loop until the game is over
while not end_of_game:
    # Get user input
    guess = input("Guess a letter: ").lower()

    # Check if user has already guessed the letter
    if guess in guessed_letters:
         print(f"You've already guessed {guess}")
    else:
        guessed_letters += guess

        # Replace underscores in display with guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Clear the terminal screen and print game logo and display
        os.system('clear')
        print(hangman_art.logo)
        print(display)        
        
        # Check if guessed letter is not in chosen word
        if guess not in chosen_word:
                    print("You guessed {guess}, that's not in the word. You lose a life.")
                    lives -= 1
                    print(hangman_art.stages[lives])

        # Check if all letters have been guessed
        if '_' not in display:
            end_of_game = True
            print("You win")

        # Check if player has no lives left
        if lives == 0:
            end_of_game = True
            print("You lose")
            print(f"The correct word is {chosen_word}")

        
