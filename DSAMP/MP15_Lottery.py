import random

rnum = []
num = int(random.randint(100, 999))
rd1 = num // 100
rnum.append(rd1)
rd2 = (num // 10) % 10
rnum.append(rd2)
rd3 = num % 10
rnum.append(rd3)
print(num)

inum = []
inp = int(input("Input Number: "))
pd1 = inp // 100
inum.append(pd1)
pd2 = (inp // 10) % 10
inum.append(pd2)
pd3 = inp % 10
inum.append(pd3)



if num == inp:
    print("You won 10000 Php!")

elif set(inum) == set(rnum):
    print("You won 3000 Php!")

else:
    pri = 0
    if pd1 in rnum:
        pri = pri + 1000
    if pd2 in rnum:
        pri = pri + 1000
    if pd3 in rnum:
        pri = pri + 1000
    print("You won {} Php!".format(pri))

