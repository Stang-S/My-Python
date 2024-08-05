def circle (r):
    area = 22/7*(r**2)
    return area

#print("circle radius %.2f" % circle(5))
r = int(input("Radius : "))
print("Circle Area = %.2f" % circle(r))