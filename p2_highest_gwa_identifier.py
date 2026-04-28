#Write a Python program that read a file containing the name of 20 students together with their GWA.
#The program will outputs the name of the student who got the highest GWA (including the GWA).

# open and read files
names_w_gwa = open("gwa.txt", "r")
gwa = []
for line in names_w_gwa:
    for char in line:
        if char.isdigit():
            number = int(char)q
            gwa.append(number)
        else:
            continue
print(gwa)