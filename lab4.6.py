#ฟังก์ชั่นหาพื้นที่วงกลม
def circle(radius):
    area = 22/7*(radius*radius)
    return area
r = int(input("รับค่ารัศมี : "))
print("พื้นที่วงกลม %.2f" % circle(r))