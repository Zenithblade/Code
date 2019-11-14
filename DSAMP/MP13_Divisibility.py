x=int(input("Enter any integer: "))

if x%5==0 and x%6==0:
    print(str(x),"is divisible by both 5 and 6")
elif x%5==0 or x%6==0:
    print(str(x),"is divisible by 5 or 6 but not both")
else:
    print(str(x),"is not divisible by either 5 or 6")