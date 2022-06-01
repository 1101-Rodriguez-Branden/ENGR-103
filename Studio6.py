#Branden Rodriguez

def input_count():#loop until enter valid entry, no input, return valid integer
    while True:
        user_input = input('Enter a value of how many numbers you want to add.')
        try:
            user_input_num = int(user_input)
            break
        except:
            print('Enter a valid integer.')
            if user_input > 0:
                print('')
    return user_input_num

def check_input_num():#check user input, no input, return valid input from user, loop until valid inut is entered.
    while True:
        user_input = input('Enter a number to add:')
        try:
            user_input_num = float(user_input)
            break
        except:
            print('Enter a valid integer')
    return user_input_num

def main ():
    user_num = input_count()
    if user_num == 0:
        print('No numbers to add, sum is 0.')
    else:
        sum_total = 0
        for counter in range(0, user_num):
            new_number = check_input_num()
            sum_total += new_number
            print('Final sum:', round (sum_total, 3))

main()