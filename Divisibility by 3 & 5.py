number = int(input("Enter a number:"))
if number%3==0 and number%5==0:
    print("The number is divisible by both 3 and 5")
elif number%3==0 and number%5!=0:
    print("The number is only divisible by 3")
elif number%3!=0 and number%5==0:
    print("The number is divisible by only 5")