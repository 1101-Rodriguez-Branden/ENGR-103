#Branden Rodriguez

O = float(input('What is the number of good parts?'))
D = float(input('What is the percentage of scrapped parts for step 1?'))
D2 = float(input('What is the percentage of scrapped parts for step 2?'))
D3 = float(input('What is the percentage of scrapped parts for step 3?'))
S = float(input('Standard time per part(in hours):'))
E = float(input('Efficiency percentage:'))
H = float(input('Hours per shift:'))
R = float(input("Percentage of reliability:"))

I = O / ((1 - D) * (1 - D2) * (1 - D3))

def calc_and_print(S, I, E, H, R):
    F = S * I / (E * H * R)
    print('The calculated required fractional machines is:', float(f'{F:.2f}'))
    print('The calculated whole number of machines is:', int(F))
calc_and_print(S, I, E, H, R)