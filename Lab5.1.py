sum = 0

def avg(num):
    score = 0
    sum = 0
    for i in range(num):
        score += int(input("Enter Number of Score %d = " % (i+1)))
        sum += score/num
    return sum

n = int(input("Enter Number of Student = "))
print("AVG Score = %.2f" % avg(n))