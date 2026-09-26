minute, second = map(int, input().split(':'))
count = 1
count += (minute//10 + minute%10)
if second < 30:
    count += (second//10)
elif second >= 30:
    count += ((second-30)//10)

print(count)