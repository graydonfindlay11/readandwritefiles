import csv 

infile = open('employeepay.csv', 'r')

csvfile = csv.reader(infile, delimiter= ',')

next(csvfile)

for record in csvfile:


    ID = record[0]
    Fname = record[1]
    Lname = record[2]
    Salary = float(record[3])
    Bonus = float(record[4])
    BonusAmt  = Bonus*Salary

    print()
    print('ID:          ', ID)
    print('First Name:  ', Fname)
    print('Last Name:   ', Lname)
    print('Salary:      ', "${:0,.2f}".format(Salary))
    print('Bonus:       ', "${:0,.2f}".format(BonusAmt))
    print('Total Pay:   ',  "${:0,.2f}".format(Salary + BonusAmt))
    enter = input()

