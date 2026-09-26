Cute_count = 0
a = int(input())
for i in range(a):
    if int(input()) == 1:
        Cute_count += 1
if Cute_count > a // 2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")