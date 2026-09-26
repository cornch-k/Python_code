result = []

for _ in range(3):
    s = input()
    leng = 1
    list_ = []
    for i in range(1, 8):

        if s[i] == s[i - 1]:
            leng += 1

        else:
            list_.append(leng)
            leng = 1
            
    list_.append(leng)
    result.append(max(list_))

print(*result, sep='\n')