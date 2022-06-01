#Branden Rodriguez

def create_list():
    list_example = 5 * [0]
    return list_example

def modify_2d(list_example, hours_input, min_input):
    # loop through elements in 1d array and turn it into a 2d array
    for list_index in range(len(list_example)):
        list_example[list_index] = [] # modify each element to be an empty list
        for list_index_2 in range(5):
            list_example[list_index].append(hours_input, min_input)
        list_example[list_index].sort()
    print(list_example)
    return list_example

list = create_list()
modify_2d(list, hours_input, min_input)

def print_2d(list_example):
    print('2D array:')
    for row in range(len(list_example)):
        if row > 0:
            print()#start new line for each row
        for col in range(len(list_example[row])): # second dimension
            #print each row on 1 line. align each colomn using f-strings
            print((f'{list_example[row][col]}'), end='')

def check_input_int(user_input_str):
    try:
        user_input = int(user_input_str)
        if user_input < 0:
            print('Enter a number larger than or equal to 0.')
            return False
        else:
            return True
    except:
        print('Enter a whole number.')
        return False

def input_class_count(day_str):
    entry_check = False
    while entry_check == False:
        print('Enter how many classes you have on', day_str, end=' ')
        user_input_str = input()
        entry_check = check_input_int(user_input_str)
    return int(user_input_str)

def check_class_times(day_str, class_id):
    print('Enter the number of hour and the number of minutes, for class', 
class_id, 'on', day_str)
    entry_check = False
    while entry_check == False:
        user_input_str = input('Hours: ')
        entry_check = check_input_int(user_input_str)
    hours_input = int(user_input_str)
    entry_check = False
    while entry_check == False:
        user_input_str = input('Minutes: ')
        entry_check = check_input_int(user_input_str)
    mins_input = int(user_input_str)
    return hours_input + mins_input / 60

def day_loop(day_str):
    day_sum = 0.0
    class_count = input_class_count(day_str)
    if class_count > 0:
        for class_id in range(1, class_count + 1):
            class_time = check_class_times(day_str, class_id)
            day_sum = day_sum + class_time
    return day_sum

def main_func():

    day_sum_mon = day_loop("Monday")
    day_sum_tue = day_loop("Tuesday")
    day_sum_wed = day_loop("Wednesday")
    day_sum_thu = day_loop("Thursday")
    day_sum_fri = day_loop("Friday")
    
    print('Monday class time is:',    round(day_sum_mon, 2), 'hours.')
    print('Tuesday class time is:',   round(day_sum_tue, 2), 'hours.')
    print('Wednesday class time is:', round(day_sum_wed, 2), 'hours.')
    print('Thursday class time is:',  round(day_sum_thu, 2), 'hours.')
    print('Friday class time is:',    round(day_sum_fri, 2), 'hours.')

    list_example = create_list()
    modify_2d(list_example, hours_input, min_input)
    print_2d(list_example)
main_func()
