a = list(map(str, input().split()))
a_1 = a.count('1')
a_2 = a.count('2')
if a_1 > a_2:
    print('1')
else:
    print('2')