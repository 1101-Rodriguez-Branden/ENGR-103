import math
import csv
col_num = 0
row_num = 0
def read_samples():
    csvfile = open('studio9.csv', 'r')
    sample_reader = csv.reader(csvfile, delimiter=',')

    sample_data = []
    row_num = 0
    for row in sample_reader:
        sample_data.append(len(row) * [])
        col_num = 0
        for col in row:
            if row[col_num] != '':
                try:
                    sample_data[row_num].append(float(row[col_num]))
                    col_num += 1
                except:
                    print('Error converting:', row[col_num], 'try again.')
                    exit()
            else:
                print('Blank entry found.')
        row_num += 1

    csvfile.close()

    return sample_data

print(read_samples)

def write_samples(sample_data,):
    csvfile = open('studio9wr.csv', 'w', newline='')
    demo_writer = csv.writer(csvfile)

    sample_num = 0
    for row in sample_data:
        print_row = []
        sample_num += 1
        print_row.append('sample#' + str(sample_num) + ':')
        demo_writer.writerow(print_row)

    def range(LB, UB, sample_average):
        if LB < sample_average < UB:
            print('All good the sample average is within the expexted range.')
        elif LB < sample_average > UB:
            print('WARNING! the sample average is above the expected range!')
        else:
            print('WARNING! the sample average is below the expected range!')
    range()

def main(col_num, row, demo_writer):
    sample_data = read_samples()

    LB = sample_average - (3 * goal_sd / math.sqrt(col_num))
    UB = sample_average + (3 * goal_sd / math.sqrt(col_num))

    csvfile = open('studio9wr.csv', 'w', newline='')
    sample_data = csv.writer(csvfile)
    print_row = [LB, goal_average, UB, range]
    demo_writer.writerow(print_row)
    for row in sample_data:
        n = len(row)
        sample_average = sum(row) / n

    try:
        goal_average =  float(input("what is the goal average value?"))
        goal_sd = float(input('What is the goal standard deviation value?'))
    except:
        print('You did not enter a number! Try again.')
    
    print(f'Lower Bound:  {LB:.2f}')
    print(f'Calculated average:  {sample_average:.2f}')
    print(f'Upper Bound:  {UB:.2f}')
    
main(col_num, row_num)