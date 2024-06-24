#ฟังก์ชั่นหาพื้นที่สามเหลี่ยม 1/2*ฐาน*สูง
def triangle(base, height):
    area = 1/2*base*height
    #print("พื้นที่สามเหลี่ยม %.2f area" % area)
    return area

print("พื้นที่สามเหลี่ยม %.3f " % triangle(2,3))