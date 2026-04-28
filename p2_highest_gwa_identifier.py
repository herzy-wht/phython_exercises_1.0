#Write a Python program that read a file containing the name of 20 students together with their GWA.
#The program will outputs the name of the student who got the highest GWA (including the GWA).

# open and read files
names_w_gwa = open("gwa_names.txt", "r")
gwa = open("gwa.txt", "w")

for line in names_w_gwa:
    for char in line:
        if char.isalpha():
            continue
        else:
            gwa.write(char)

gwa.close()
names_w_gwa.close()