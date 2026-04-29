#P3. Write a method in python to write multiple line of text contents into a text file mylife.txt.

file_name = open("mylife.txt", "r")

question = "y"

while question == "y" :
    text = str(input("Enter Line: "))
    question = str(input("Are there more lines y/n? "))
