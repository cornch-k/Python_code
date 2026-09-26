n = int(input())

for i in range(n):
    string = input()
    sorted(string)
    result = 0

    for j in range(65, 91):
        if string.find(chr(j)) == -1:
            result += j
        else:
            continue
    print(result)