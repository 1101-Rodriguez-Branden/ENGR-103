import random
num = random.randint(1, 10)

answers = 5
while answers > 0: #get guesses to stop after 5 attempts
    guess = int(input('Guess a number between 1-10?'))
    if guess == num:
        print('That is correct!')
        exit()
    else:
        print('Wrong, guess again!')#find end program
        answers = answers - 1
print(f"You ran out of guesses! The number was {num}.")
exit()