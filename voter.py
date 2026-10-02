try:
    age = int(input("Enter the age of the person: "))
    if age >= 18:
        print("Eligible to cast vote!")
    else:
        print("Not eligible to cast vote!")
except ValueError:
    print("Please enter a valid number.")