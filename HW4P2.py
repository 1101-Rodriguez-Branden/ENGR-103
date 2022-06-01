import random as r
import string
 
# index 0 is license, 1 is title, 2 is test
time_list = [5.97, 18.63, 36.21]
 
def num_customers():
   customers = input('Enter the number of customers: ')
   flag = 0
   while flag == 0:
       try:
           if int (customers) < 0:
               print('Your input is invalid. Enter positive number.\n')
               customers = input('Enter the number of customers: ')
           elif int (customers) > 0:
               flag = 1
               return int (customers)
       except:
           print('Your input is not a number or has a decimal. Enter a number.\n')
           customers = input('Enter the number of customers: ')
 
 
 
def num_servers():
   servers = input('Enter the number of servers: ')
   flag = 0
   while flag == 0:
       try:
           if int (servers) < 0:
               print('Your input is invalid. Enter positive number.\n')
               servers = input('Enter the number of servers: ')
           elif int (servers) > 0:
               flag = 1
               return int (servers)
       except:
           print('Your input is not a number or has a decimal. Enter a number.\n')
           servers = input('Enter the number of servers: ')
 
 
 
def shift_length():
   shift = input('Enter the length of the shift in minutes: ')
   flag = 0
   while flag == 0:
       try:
           if int (shift) < 0:
               print('Your input is invalid. Enter positive number.\n')
               shift = input('Enter the length of the shift in minutes: ')
           elif int (shift) > 0:
               flag = 1
               return int (shift)
       except:
           print('Your input is not a number or has a decimal. Enter a number.\n')
       shift = input('Enter the length of the shift in minutes: ')
 
 #n = 'emply time'.rjust(.5)
 #string.rjust(.4)
 
 
def create_server_num(customers):
   server_num = [0] * customers
   for x in range(len(server_num)):
       num = r.randint(1,11)
       print(num)
       if num < 6:
           server_num[x] = 0
       elif  5 < num < 9:
           server_num[x] = 1
       else:
           server_num[x] = 2
   return server_num
 
def create_customer_choice_list(servers, server_num):
   customer_choice_list = [0] * servers
   print(server_num)
   for x in range(len(server_num)):
       server_choice = customer_choice_list.index(min(customer_choice_list))
       print(server_choice)
       customer_choice_list[server_choice] = customer_choice_list[server_choice] + time_list[server_num[x]]
       print(customer_choice_list)
   return customer_choice_list
 
def main_function():
 
    customers = num_customers()
    servers = num_servers()
    shift = shift_length()
    server_num = create_server_num(customers)
    create_customer_choice_list(servers, server_num)
    #utilization = x / s
    print('Customer ID              Service ID             Server Number             Ending Time')
    for x in range(len(server_num)):
        print(server_num)
 
    print('Server Number               Ending Time             Utilization %' )
 
main_function()
 
 

