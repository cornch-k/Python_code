min = 0
sum = 0
count = 0

while count != 4:
    a = int(input())
    sum +=a
    count += 1

min = sum // 60
sum -= min*60

print(min)
print(sum)