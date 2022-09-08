import csv

from signal import default_int_handler


infile = open('steps.csv', 'r')
outfile = open("avg_steps.csv",'w')

csvfile = csv.reader(infile, delimiter= ',' )

next (csvfile)

step_counter = 0
i = 0

outfile.write("Month, Average Steps\n")

month = 1
month_names=['January','February','March','April','May','June','July','August',
              'September','October','November','December']





for record in csvfile:
    print(i)
    if float(record[0])!= month:
        
        month -= 1
        avg = (step_counter/i)
        avg = format(avg,',.2f')

        print(month_names [month]+ ', ' + str(avg))

        outfile.write(month_names [month] + ':   \t' + str(avg)+ '\n')

        month += 2
        i = 0
        step_counter = 0


    if float(record[0]) == month:
        i += 1 
        step_counter += float(record[1])
        

        
outfile.close()



