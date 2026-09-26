a = input()
b = list()

for i in range(len(a)):
    b.append(int(a[i]))
b.sort(reverse=True)

for j in b:
    print(j, end="")
print()