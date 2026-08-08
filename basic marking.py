x = float(input("Enter the marks of the student in a subject: "))
if 90 <= x <= 100:
    print("The grade of the student is A")
elif 80 <= x < 90:
    print("The grade of the student is B")
elif 70 <= x < 80:
    print("The grade of the student is C")
elif 60 <= x < 70:
    print("The grade of the student is D")
else:
    print("The student has failed")