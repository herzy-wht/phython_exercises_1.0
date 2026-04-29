#Write a Python program that read a file containing the name of 20 students together with their GWA.
#The program will outputs the name of the student who got the highest GWA (including the GWA).

class StudentGWA:
    def find_highest(self):
        names_w_gwa = open("gwa_names.txt", "r")

        highest_gwa = 0
        highest_gwa_name = ""

        for line in names_w_gwa:
            name = ""
            gwa = ""

            for char in line:
                if char.isalpha() or char == " ":
                    name += char
                else:
                    gwa += char

            gwa = int(gwa)

            if gwa > highest_gwa:
                highest_gwa = gwa
                highest_gwa_name = name
        names_w_gwa.close()

        print(highest_gwa_name,highest_gwa)

student = StudentGWA()
student.find_highest()