a = list()
max_num = 0
init_num = 0
for i in range(4):
    minus, plus = map(int, input().split())
    init_num -= minus
    a.append(init_num)
    init_num += plus
    a.append(init_num)
    max_num = max(a)
print(max(a))