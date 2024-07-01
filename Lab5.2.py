def Ecom(n):
    sum = 0
    vat = 0
    price = 0
    for i in range(n):
        price += int(input("Enter price %d = " % (i+1)))
        vat = price*(7/100)
        sum = vat + price
    return sum

def cash(p,m):
    c = p - m
    return m

n = int(input("Enter number of thing = "))
print("Price + Vat 7 = %.2f" % Ecom(n))
p = % Ecom(n)
m = float(input ("Enter money = "))
print("Cash = %.2f" %cash(m))