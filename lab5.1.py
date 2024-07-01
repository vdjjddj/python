def score(n):
    
    sum_score = 0
    
    for i in range(n):
        score = int(input(f"กรอกคะแนนนักศึกษาคนที่ {i+1}: "))
        sum_score += score
        
        avgscore = sum_score/n
    return avgscore
    
n = int(input("กรอกจำนวนนักศึกษา: "))
average = score(n)
print(f"คะแนนเฉี่ลยของนักศึกษา {n} คน คือ {average}")