import sys
d = int(sys.stdin.readline())

d = bin(d)

num = str(d[2:])
num = '0b' + num[::-1]
print(int(num, 2))