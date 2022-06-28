
'''
for this exercise:
    Write a function (guessing_game) that takes no arguments.
 When run, the function chooses a random integer between 0 and 100 (inclusive).
3EXERCISE 1 ■ Number guessing game
 Then ask the user to guess what number has been chosen.
 Each time the user enters a guess, the program indicates one of the following:
– Too high
– Too low
– Just right
 If the user guesses correctly, the program exits. Otherwise, the user is asked to
try again.
 The program only exits after the user guesses correctly

'''
#camelCase >>> snake_case :-)


import random

def guessingGame():

    correctAnswer = random.randint(1,100)

    


    guessIsCorrect = False

    x = 0

    while x != 1:
        guess = int(input('input your guess'))

        if guess == correctAnswer:
            print(f'Correct! The answer is {correctAnswer}')
            x=1
            break


        if guess > correctAnswer:
            print(f'Your guess ({guess}) is too high.')

    
        else:
            print(f'Your guess ({guess}) is too low.')


guessingGame()



