Seconds=int(input("Enter the time in seconds: "))
Hour = Seconds//(60*60)
Minutes = (Seconds//60)%60
Seconds = Seconds%60
print("The time in hour:minutes:seconds format is:", Hour, ":", Minutes, ":", Seconds)
