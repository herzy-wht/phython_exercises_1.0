#Write a Python program that read a file containing the name of 20 students together with their GWA.
#The program will outputs the name of the student who got the highest GWA (including the GWA).

# open and read files
names_w_gwa = open("gwa_names.txt", "r")

highest_gwa = 0
highest_gwa_name = ""

for line in names_w_gwa:
    data = line.strip().split(",")
    name = data[0]
    gwa = float(data[1])

    if gwa > highest_gwa:
        highest_gwa = gwa
        highest_gwa_name = name

names_w_gwa.close()