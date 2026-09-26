a = int(input())
b = input()
ans = 0
for i in range(a):
    ans += (ord(b[i]) - 64)
print(ans)