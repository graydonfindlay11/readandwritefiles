# This program reads and displays the contents
 # of the philosophers.txt file.
def main():
 # Open a file named philosophers.txt.
        infile = open('philosophers.txt', 'r')
 
    

 # Read the file's contents.
       # file_contents = infile.read()
        line1 = infile.readline().rstrip('\n')
        line2 = infile.readline().rstrip('\n')                   #RSTRIP METHOD ONLY APPLIES TO READLINE (NOT INFILE READ)
        line3 = infile.readline().rstrip('\n')

# Print the data that was read into memory.    --- YOU DONT HAVE TO CLOSE THE FILE WHEN JUST READING IT
        #print (file_contents)
        print (line1)
        print (line2)
        print (line3)
main()

