import random

choices=["scissor","rock","paper"]
num = int(random.randint(0, 2))
end=choices[num]
print(end)

player=int(input("scissor(0),rock(1),paper(2): "))
pld=choices[player]

if end == pld:
    endstr=('It is a draw')

else:
    if pld == choices[0]:
        if end == choices[2]:
            endstr = ('You won')
        elif end == choices[1]:
            endstr = ('You lose')
    if pld == choices[1]:
        if end == choices[0]:
             endstr = ('You won')
        elif end == choices[2]:
             endstr = ('You lose')
    if pld == choices[2]:
        if end == choices[1]:
             endstr = ('You won')
        elif end == choices[0]:
             endstr = ('You lose')

print ("The computer is {}. You are {}.".format(end,pld) + endstr)