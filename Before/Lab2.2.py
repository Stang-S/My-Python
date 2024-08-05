s = (input("ใส่ค่าคะแนน : "))
if s < 0 :
    print("กรุณากรอกข้อมูล 0-100")
elif s > 100:
    print("กรุณากรอกข้อมูล 0-100")
elif s <= 49:
    print("เกรด F")
elif s <= 59:
    print("เกรด D")
elif s <= 69:
    print("เกรด C")
elif s <= 79:
    print("เกรด B")
elif s <= 100:
    print("เกรด A")
else :
    print("กรุณากรอกข้อมูล 0-100")