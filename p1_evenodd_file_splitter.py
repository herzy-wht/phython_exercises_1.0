#P-1. Write a Python program that reads a text file named numbers.txt
#that contains 20 integers. The program will create two other text file; the first text file
#will be named even.txt that will contains all even numbers extracted from the numbers.txt.
#The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt

#open and read file
class NumberSorter:
    def separate(self):
        # open files
        source = open("numbers.txt", "r")
        #create files for odd and even
        even = open("even.txt", "w")
        odd = open("odd.txt", "w")

        # check each number if even or odd
        for line in source:
            num = int(line)

            if num % 2 == 0:
                even.write(line)
            else:
                odd.write(line)

        # close files
        source.close()
        even.close()
        odd.close()


# create object
file = NumberSorter()

# run method
file.separate()