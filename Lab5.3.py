H = int(input("Home work = "))
M = int(input("Mid term = "))
F = int(input("Final = "))

sum = H + M + F
print("คะแนน = %.2f"% sum)
if sum > 100:
    print("ขี้โม้")
if sum >= 80 and sum < 101:
    print("มากกว่า 80 คะแนน ดีมาก")
if sum > 50 and sum < 80:
    print("มากกว่า 50 คะแนน ผ่าน")
if sum < 50:
    print("น้อยกว่า 50 คะแนน ไม่ผ่าน")