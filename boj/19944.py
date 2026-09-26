N, M = map(int, input().split())
#M이 학생의 학년, N이 기준학년
if M == 1 or M ==2:
    print("NEWBIE!")
elif M > 2 and M <= N:
    print("OLDBIE!")
else:
    print("TLE!")