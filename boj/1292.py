a, b = map(int, input().split())

array = [0]
for i in range(46):
    for j in range(i):
        array.append(i)

print(sum(array[a:b+1]))
