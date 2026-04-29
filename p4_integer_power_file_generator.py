#p4. Write a method in python that will create two separate text files after reading the source text file named integers.txt thant contains 20 integers.
# The first output file will be named double.txt containing the square of all even integers found in integers.txt and the second file will be named
# triple.txt containing the cube of all odd numbers found in the integers.txt.

class IntegerFileProcessor:
    def __init__(self):
        self.file_integers = open("integers.txt", "r")
        self.double_integers = open("double.txt", "w")
        self.triple_integers = open("triple.txt", "w")

    def process_files(self):
        for line in self.file_integers:
            line = int(line)
            if line % 2 == 0:
                square = line**2
                square = str(square)
                self.double_integers.write(square)
                self.double_integers.write("\n")
            else:
                cube = line**3
                cube = str(cube)
                self.triple_integers.write(cube)
                self.triple_integers.write("\n")

        self.file_integers.close()
        self.double_integers.close()
        self.triple_integers.close()

integers = IntegerFileProcessor()
integers.process_files()
