def cal (wt, he):
    bmi = wt/(he**2)
    return bmi

def ref (bmi):
    if bmi < 18.50:
        print("น้ำหนักน้อย/ผอม")
    elif bmi >= 18.50 and bmi <= 22.90:
        print("ปกติ/สุขภาพดี")
    elif bmi >= 23.00 and bmi <= 24.90:
        print("ท้วม/โรคอ้วนระดับ 1")
    elif bmi >= 25.00 and bmi <= 29.90:
        print("อ้วน/โรคอ้วนระดับ 2")
    elif bmi > 30.00:
        print("อ้วนมาก/โรคอ้วนระดับ 3")

wt = float(input("Weight = "))
he = float(input("Height =  "))
print("BMI = %.2f" % cal(wt,he))
bmi = wt/(he**2)
print(ref(bmi))