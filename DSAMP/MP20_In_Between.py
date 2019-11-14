import random

n1 = random.randint(1,13)
n2 = random.randint(1,13)

print (n1)
print (n2)

if n1 == n2:
    x = str(input("Higher or Lower? "))
    if x.lower() == "higher":
        n3 = random.randint(1, 13)
        if n3 > n1 and n3 > n2:
            print(n3)
            print("You Win!")
        else:
            print(n3)
            print("You Lose!")
    elif x.lower() == "lower":
        n3 = random.randint(1, 13)
        if n3 < n1 and n3 < n2:
            print(n3)
            print("You Win!")
        else:
            print(n3)
            print("You Lose!")

else:

    if n1 > n2:
        hn = n1
        ln = n2
    elif n2 > n1:
        hn = n2
        ln = n1

    x = str(input("Deal or No Deal? "))
    if x.lower() == "deal":
        n3 = random.randint(1, 13)
        if ln < n3 < hn:
            print(n3)
            print("You Win!")
        else:
            print(n3)
            print("You Lose!")
    elif x.lower() == "no deal":
        print("You Lose!")

