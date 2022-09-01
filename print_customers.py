import csv 

infile = open('customers.csv', 'r')

csvfile = csv.reader(infile, delimiter= ',')

next(csvfile)

for record in csvfile:


    ID = record[0]
    Fname = record[1]
    Lname = record[2]
    City = record[3]
    Country = record[4]
    Phone = record[5]
    
    print(' ID:         ', ID + '\n',
         'First Name: ', Fname + '\n',
         'Last Name:  ', Lname + '\n',
         'City:       ', City + '\n',
         'Country:    ', Country + '\n',
         'Phone Num:  ', Phone + '\n')
    




