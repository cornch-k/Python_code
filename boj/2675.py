# 2675
Run_num = int(input())
i = 0


while i < Run_num:
    num, string = input().split()
    num = int(num)
    string = string.upper()
    string = list(string)
    j = 0
    string_list = []


    for j in range(0, len(string)):
        string_list.append(string[j] * num)
    i += 1