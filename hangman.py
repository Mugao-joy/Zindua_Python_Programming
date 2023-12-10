"""Choose some good hangman words for your program. You can go to this website and create a list of words for your game.

At the start of the game, use the random library to choose a random word from your hangman words and display the word's letters as dashes rather than letters.

Now, apply the input function to allow the user to make letter guesses. Use try... except and if statements to ensure that only valid inputs work with your script i.e. a user can only choose one letter at a time, and a user cannot choose letters that have been selected before.

If the letter is in the word, it is printed in place of the corresponding dash. If the letter is not in the word, that is counted as a failed attempt, Limit the number of failed attempts for the user to 6 such that on the 6th fail, the game ends, and the script prints the actual word and "You Lost". Make sure to tell the user they won if they guess all the correct letters in under 6 failed attempts.

If you want to take the project a notch higher, you can use the Python Turtle Library to visualize the hanging like on this website. This is optional!"""

import random
import os
words = ['man', 'cave','zebra', 'cat', 'mouse']
random_words = random.choice(words)
print(random_words)
hidden_word = ['_'] * len(random_words)

failed_attempts = 0
guessed_characters = []

while ['_'] in hidden_word and failed_attempts < 6:
    print(hidden_word)
    print ('Already selected characters: ', guessed_characters)
    guessed = input('Enter a character: ')

    if len(guessed) != 1:
        os.system('cls')
        print('You cannot insert two or more characters')
    if guessed in guessed_characters:
        print('You have already selected this character')
        os.system('cls')
        continue
    
    guessed_characters.append(guessed)
    if guessed in random_words:
        for i in range(len()):
            if random_words[i] == guessed:
                hidden_word[i] == guessed
                os.system('cls')
    else:
        os.system('cls')
        failed_attempts += 1