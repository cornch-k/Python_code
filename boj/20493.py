import sys
input = sys.stdin.readline

N, T = map(int, input().split())

d = [(1, 0), (0, -1), (-1, 0), (0, 1)]

i = X = Y = 0
li = [0]

for j in range(N):
    time, s = map(str, input().split())

    time = int(time)
    t = time-li[-1]
    li.append(time)

    x, y = d[i][0], d[i][1]
    X += t * x; Y += t * y
    i += 1 if s == 'right' else -1
    i %=  4

t = T - li[-1]
x, y = d[i][0], d[i][1]
X += t * x; Y += t * y

print(X, Y)