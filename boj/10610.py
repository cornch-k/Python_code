num = list(input())
sum = 0

num.sort(reverse=True)

for i in num:
    sum += int(i)
    
if sum % 3 != 0 or "0" not in num:
    print(-1)
else:
    for i in num:
        print(i, end = "")