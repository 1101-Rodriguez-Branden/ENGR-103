#Branden Rodriguez
import math

def main():
    
    x1 = func1('What is the x1 sample?')
    x2 = func1('What is the x2 sample?')
    x3 = func1('What is the x3 sample?')
    x4 = func1('What is the x4 sample?')
    x5 = func1('What is the x5 sample?')
    goal_average = func1('what is the goal average value?')
    goal_sd = func1('What is the goal standard deviation value?')
    
def func1(msg):
    while True:
        user_input = input(msg)
        try:
            user_input = float(user_input)

            if  user_input > 0:
                break
            else:
                print('Your numnber is less than 0! Try again.')
        except:
            print('Invalid entry, enter a number.')
    return user_input

sample_average = func1(x1 + x2 + x3 + x4 + x5) / 5
LB = sample_average - (3 * goal_sd / math.sqrt(5))
UB = sample_average + (3 * goal_sd / math.sqrt(5))
 
print(f'Lower Bound:  {LB:.2f}')
print(f'Calculated average:  {sample_average:.2f}')
print(f'Upper Bound:  {UB:.2f}')
 
def range():
    if LB < sample_average < UB:
        print('All good the sample average is within the expexted range.')
    elif LB < sample_average > UB:
        print('WARNING! the sample average is above the expected range!')
    else:
        print('WARNING! the sample average is below the expected range!')
range()
main()