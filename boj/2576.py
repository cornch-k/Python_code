num_list = []
odd_list = []
count = 0
result = 0

while count != 7:
    a = int(input())
    num_list.append(a)
    count += 1

for i in range(len(num_list)):
    if num_list[i] % 2 == 0:
        continue
    else:
        odd_list.append(num_list[i])

for j in range(len(odd_list)):
    result += odd_list[j]

if len(odd_list) == 0:
    print(-1)
else:
    odd_list.sort()
    print(result)
    print(odd_list[0])