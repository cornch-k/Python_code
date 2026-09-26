h, m, s = int(input().split())
time = int(input())

if time < 60:
    s += time
    if s >= 60:
        s -=60
        m += 1
elif time 