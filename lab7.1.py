def salary(name, salary, overtime):
    if(overtime>40):
        overtimes=overtime*150
    else:
        overtimes=overtime*100
    total = salary+overtimes
    print("คุณ %s" %name)
    print("เงินเดือน %.2f" %salary)
    print("ชั่วโมงล่วงเวลา %d" %overtime)
    print("เงินล่วงเวลา %.2f" %overtimes)
    print("เงินเดือนทั้งหมด %.2f" %total)
    
    
n = input("ชื่อ : ")
s = int(input("เงินเดือน : "))
o = int(input("ชั่วโมงล่วงเวลา : "))
salary(n,s,o)
        