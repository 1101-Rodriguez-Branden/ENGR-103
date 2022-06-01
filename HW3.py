#Branden Rodriguez
##################################################################
# Function:
# Description:
# Parameters:
# Return values:
# Pre-conditions:
# Post-conditions:
##################################################################
def check_error(goal, first, slope):
    while True:
        if goal <= 0:
           print('Your goal cycle must be greater than 0. Try again.')
        elif goal >= first:
           print('Your goal cycle must be less than your first cycle time. Try again.')
        else:
            break
 
    while True:
        if slope >= 0:
            print('Your slope must be less than 0. Try again.')
        else:
            break
check_error()
#################################################################
# Function:
# Description:
# Parameters:
# Return values:
# Pre-conditions:
# Post-conditions:
##################################################################
def math(goal, first, slope):
# maybe use a while loop to tell the loop to run and stop when it reaches goal, put for loop inside while loop for it to run through cycles
   number_cycle = 1
   cycle_time = 0
   learn = 2 ** slope
   while True:
       cycle_time = first * (number_cycle ** slope)
       if cycle_time > goal:
           print(f'Cycle:{number_cycle:.0f}    Time:{cycle_time:.3f}')
           number_cycle = number_cycle + 1
       else:
           return print(f'Desired cycle time has been achieved!   Learning percent is: {learn:.2f}')
#################################################################
# Function:
# Description:
# Parameters:
# Return values:
# Pre-conditions:
# Post-conditions:
##################################################################
def main():
   goal = float(input('Enter the goal cycle time in minutes:'))
   first = float(input('Enter the first cycle time in minutes:'))
   slope = float(input('Enter the slope as a number less than 0:'))
   math(goal, first, slope)
   check_error(goal, first, slope)
main()
 
 
 
 
 

