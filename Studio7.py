#Branden Rodriguez
import random as r

##################################################################
# Function: Create_list_append
# Description: appends the list
# Parameters: none
# Return values: list_example
# Pre-conditions:none
# Post-conditions:none
##################################################################
def create_list_append():
    list_example = []
    for list_index in range (10):
        list_example.append(0) #append you do not use indedx value
    print('in append:', list_example)
    return list_example
##################################################################
# Function: create_list_loop
# Description: creates the loop with 10 elements.
# Parameters: none
# Return values: create_list_loop
# Pre-conditions: none
# Post-conditions: none
##################################################################
def create_list_loop():
    list_example = [0] * 10
    for list_index in range(10):
        list_example[list_index] = 1 #to use index value, use square brackets
    print('in loop for index:', list_example)

create_list_loop()
##################################################################
# Function: Modify_list
# Description:changes list to random values between 1-100
# Parameters:list_example
# Return values:print('in modify')
# Pre-conditions: list example, list index
# Post-conditions:none
##################################################################
def modify_list(list_example):
    for list_index in range(len(list_example)):
        list_example[list_index] = r.randint(1,100)
    print('in modify:', list_example)
##################################################################
# Function: guess
# Description: user guesses 5 times
# Parameters:list_example
# Return values:ran out of guesses
# Pre-conditions:list_examples
# Post-conditions:
##################################################################
def guess(list_example):
    answers = 5
    while answers > 0: #get guesses to stop after 5 attempts
        guess = int(input('Guess a number between 1-10?'))
        if guess in list_example:
            print(f'That is correct! the answers are {list_example}')
            exit()
        else:
            print('Wrong, guess again!')#find end program
            answers = answers - 1
    print(f"You ran out of guesses! The numbers were {list_example}.")
##################################################################
# Function: create_list
# Description: calls all of the previous functions and excecutes them
# Parameters:none
# Return values:create list
# Pre-conditions:list_example
# Post-conditions:none
##################################################################
def create_list():
    list_example = create_list_append()
    print('in create:', list_example)

    create_list_loop()
    print('in create:', list_example)

    modify_list(list_example)
    print('in create:', list_example)

    guess(list_example)
    print('in create:', list_example)

create_list()


