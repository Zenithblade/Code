point = tuple(map(float, input("Enter x and y coordinate: ").split()))

cpt = (0, 0)
radius = 10.0

area = ((((point[0] -cpt[0]) ** 2)+((point[1] -cpt[1]) ** 2)) ** 0.5)

if int(area) <= radius:
    print("Point X at {} is inside the circle".format(str(point)))
else:
    print("Point X at {} is outside the circle".format(str(point)))
