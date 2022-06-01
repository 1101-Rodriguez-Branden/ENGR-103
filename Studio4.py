#Branden Rodriguez
def compare():
    air = input('What is the air quality rating?')
    try:
        air = float(air)
    except:
            print('invalid input, try again.')
    if air < 0:
        print("error")
    elif air <= 50 :
        print("Good.")
        
    elif air <= 100:
        print('Moderate.')
        
    elif air <= 150:
        print("Unhealthy, for sensitive groups.")

    elif air <= 200:
        print("Unhealthy.")

    elif air <= 300:
        print("Very unhealthy.")

    elif air<= 500:
        print("Hazardous.")
    else:
        print("error")
    return compare
def main():
    compare()
main()