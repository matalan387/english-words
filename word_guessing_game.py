import random

WORDS = [one_word.strip()
         for one_word in open('words.txt')]


def guessing_game():
    answer = random.choice(WORDS)

while True:
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            print(f'Right!  The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')
