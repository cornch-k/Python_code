a = int(input())
for i in range(a):
    animal = dict()
    txt = input().split()
    result = []
    while True:

        s = input()
        if s[:5] == 'what ':
            break
        s = s.split()
        animal[s[2]] = s[0]
 
    for i in txt:
        if i not in animal:
            result.append(i)
 
    for i in result:
        print(i, end=' ')