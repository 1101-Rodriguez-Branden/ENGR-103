
Miles = 100000
Price = float(input("Price of gas:"))
mpg = int(input("What is the miles per gallon?"))
gallonsUsed = Miles/ mpg
def calc_and_print(Price, gallonsUsed): 
    totalPrice = Price * gallonsUsed
    roundedPrice = round(totalPrice, 2)
    print("Gallons used over 100,000 miles:", totalPrice)
calc_and_print(Price, gallonsUsed)