#P-1. Write a Python program that reads a text file named numbers.txt
#that contains 20 integers. The program will create two other text file; the first text file
#will be named even.txt that will contains all even numbers extracted from the numbers.txt.
#The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt

#open and read file
numbers_file = open('numbers.txt', 'r')
even_file = open('even.txt', 'w')
odd_file = open('odd.txt', 'w')

for line in numbers_file:
    number = int(line)
    if number % 2 == 0:
        even_file.write(line)
    else:
        odd_file.write(line)
        
even_file.close()
odd_file.close()
numbers_file.close()

