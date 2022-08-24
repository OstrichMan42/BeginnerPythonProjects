import random
from re import L
from tokenize import String
import string

# string concatenation
def MadLibs():
    adj = input("Adjective: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    famous_person = input("Famous Person: ")


    madlib = f"Computer programing is so {adj}! It makes me so excited all the time because\
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"


    print(f"oh my {madlib}")


# Random numberr
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, too low!")
        elif guess > random_number:
            print("Sorry too high")
    print("You got it!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if (low != high):
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1

    print(f"Aha! I knew it! {guess}!")


def rps():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return f'You won! Computer played {computer}'
    
    return f'You lost :( Computer played {computer}'

# Did player1 beat player2?
def is_win(player1, player2):
    return ((player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p') or (player1 == 'p' and player2 == 'r'))




from words import words
# filter words that have non-letters
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    secretWord = get_valid_word(words)
    word_letters = set(secretWord) # set of letters in word
    alphabet = set(string.ascii_lowercase)
    used_letters = set()

    lives = 5


    while len(word_letters) > 0 and lives > 0:
        
        print("You have used these letters: ", ' '.join(used_letters))
        
        currentWord = ''.join([letter if letter in used_letters else '_' for letter in secretWord])
    
        # Get user input
        user_letter = input(f'Find the word; {currentWord}\
            Guess a letter: ').lower()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print(f"You guessed wrong, you have {lives} lives left")
        
        elif user_letter in used_letters:
            print("You already used that one")
        else:
            print("invalid response")

    if lives != 0:
        print(f"Conglaturations you guessed the word {secretWord}")
    else:
        print(f"Oof, it was {secretWord}")


hangman()