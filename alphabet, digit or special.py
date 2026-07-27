n=(input("Enter an input : "))
if (n>='a' and n<='z') or (n>='A' and n<='Z'):
    print(n, "is an alphabet")
elif(n>='0' and n<='9'):
    print(n, "is a digit")
else:
    print(n, "is a special character")
    