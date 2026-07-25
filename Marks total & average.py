def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter the marks of {subject} out of 100: "))
            if 0 <= marks <= 100:
                return marks
            print("Please enter the marks out of 100")
        except ValueError:
            print("Please enter a valid number")


Maths = get_valid_marks("Maths")
Science = get_valid_marks("Science")
English = get_valid_marks("English")
Second_Language = get_valid_marks("Second Language")
Evs = get_valid_marks("EvS")

Total = Maths + Science + English + Second_Language + Evs
Average = Total / 5
print("The total marks of the student out of 500 is:", Total)
print("The average marks of the student is:", Average)
print("The percentage obtained by the student is:", Average, "%")

