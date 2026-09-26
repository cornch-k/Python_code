N, K = map(int, input().split())
ysps_list = list()

for i in range(1, N+1):
    ysps_list.append(i) #원 사람


kill = 0 #죽일 사람
seq = list() # 죽은 순서

for i in range(N):
    kill += K-1
    if kill >= len(ysps_list): #한 바퀴 돌고 그 다음으로 돌아올 때를 대비해 값을 나머지로 바꿈.
        kill %= len(ysps_list)

    seq.append(str(ysps_list.pop(kill)))

print("<", end = "")
for i in range(len(seq) - 1):
    print(seq[i], end = ", ")
print(f"{seq[-1]}>")