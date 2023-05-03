# Hangman Game

This is a simple implementation of the classic Hangman game in Python. The program selects a random word from a pre-defined list of words, and the user must guess the letters of the word one at a time. The user has a limited number of guesses, and loses the game if they fail to guess the word before running out of guesses.

## Getting Started

To run the Hangman game on your local machine, you will need to have Python 3 installed. You can download Python 3 from the [official website](https://www.python.org/downloads/).

Once you have installed Python 3, you can clone this repository to your local machine and run the `hangman.py` file using the following command:

python3 hangman.py


## How to Play

The game will randomly select a word from the pre-defined list of words, and display the number of letters in the word as underscores.

You will be prompted to guess a letter. Type in a letter and press Enter.

If your guess is correct, the corresponding letter(s) in the word will be revealed. If your guess is incorrect, you will lose a life.

You have a limited number of lives, indicated by the number of stages of the hanging man that are displayed. If the hanging man is fully drawn, you lose the game.

Continue guessing letters until you correctly guess the word, or run out of lives.

## Credits

This project was created by Amal Lal and is based on the Hangman project from The Odin Project.

The following resources were used in the development of this project:

- Python 3
- random module in Python
- os module in Python

Special thanks to Angela Yu for providing the 100 Days of Code course on Udemy, which inspired this project.

The ASCII art used in this project was created by Christopher Johnson. The word list used in this project was provided by The Hangman Project.

Thanks to all these people and organizations for their contributions to the development of this project.

