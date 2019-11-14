cons = list(map(float, input("Enter a, b, c, d, e, f: ").split()))

#a = cons[0]
#b = cons[1]
#c = cons[2]
#d = cons[3]
#e = cons[4]
#f = cons[5]

d=(cons[0]*cons[3]) - (cons[1]*cons[2])

if d == 0:
    print("No Solution")
else:
    x = ((cons[4] * cons[3]) - (cons[1] * cons[5])) / (d)
    y = ((cons[0] * cons[5]) - (cons[4] * cons[2])) / (d)
    print("x is {} and y is {}.".format(x, y))