point1 = list(map(float, input("Enter x and y coordinate: ").split()))
point2 = list(map(float, input("Enter x and y coordinate: ").split()))

dist = (((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5)


print(dist)