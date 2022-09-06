import csv

infile = open('customers.csv', 'r')

csvfile = csv.reader(infile, delimiter= ',' )

next (csvfile)

print()
print('FULL NAME, COUNTRY')
print('------------------')
print()
i = 0
for record in csvfile:

    ID = record[0]
    Fname = record[1]
    Lname = record[2]
    City = record[3]
    Country = record[4]
    Phone = record[5]


    print(Fname + ' ' + Lname, end='')
    print(', '+ Country + '\n')
    i += 1
print("Number of Customers: ", i)
print()





