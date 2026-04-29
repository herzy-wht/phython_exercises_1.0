#p4. Write a method in python that will create two separate text files after reading the source text file named integers.txt thant contains 20 integers.
# The first output file will be named double.txt containing the square of all even integers found in integers.txt and the second file will be named
# triple.txt containing the cube of all odd numbers found in the integers.txt.

file_integers = open("integers.txt", "r")
double_integers = open("double.txt", "w")
triple_integers = open("triple.txt", "w")

for line in file_integers:
    line = int(line)
    if line % 2 == 0:
        square = line**2
        double_integers.write(square)
    else:
        cube = line**3
        triple_integers.write(cube)

file_integers.close()
double_integers.close()
triple_integers.close()


