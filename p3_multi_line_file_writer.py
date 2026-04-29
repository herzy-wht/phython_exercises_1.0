#P3. Write a method in python to write multiple line of text contents into a text file mylife.txt.

class MyLifeFile:
    def __init__(self):
        self.file_name = open("mylife.txt", "w")
        self.question = "y"

    def write_lines(self):
        while self.question == "y" :
            text = str(input("Enter Line: "))
            self.file_name.write(text)
            self.file_name.write("\n")
            self.question = str(input("Are there more lines y/n? "))

        self.file_name.close()

lines = MyLifeFile()
lines.write_lines()
