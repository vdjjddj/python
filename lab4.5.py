def triangle(base, height):
    area = 1/2*base*height
    return area
b=int(input("ค่าฐาน:"))
h=int(input("ค่าสูง:"))
print("พื้นที่สามเหลี่ยม%.3f" % triangle(b,h))