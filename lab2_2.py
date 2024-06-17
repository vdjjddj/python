x=int(input("รับค่าคะแนน"))
if x >= 80 and x <= 100:
    print("เกรดA")
elif x >= 70 and x <= 79:
    print("เกรดB")
elif x >= 60 and x <= 69:
    print("เกรดC")
elif x >= 50 and x <= 59:
    print("เกรดD")
elif x >= 0 and x <= 49:
    print("เกรดF")
else:
    print("กรุณากรอกข้อมูล0-100")