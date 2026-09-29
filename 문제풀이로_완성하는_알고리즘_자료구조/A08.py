H, W = map(int, input().split())
matlist = list()
for i in range(H):
    matlist.append(list(map(int, input().split())))


# 2차원 배열 만들기
matlist.insert(0, [0] * (W + 1))
for i in range(1, H + 1):
    matlist[i].insert(0, 0)

# 누적합 배열만들기
prefixList = list()
for i in range(H + 1):
    prefixList.append([0] * (W + 1))


for i in range(1, H + 1):  # 가로방향 누적합 구하기
    for j in range(1, W + 1):
        prefixList[i][j] = prefixList[i][j - 1] + matlist[i][j]

for i in range(1, H + 1):  # 아래방향 누적합 구하기
    for j in range(1, W + 1):
        prefixList[i][j] = prefixList[i - 1][j] + prefixList[i][j]

Q = int(input())
for i in range(Q):
    A, B, C, D = map(int, input().split())
    print(
        prefixList[C][D]
        + prefixList[A - 1][B - 1]
        - prefixList[A - 1][D]
        - prefixList[C][B - 1]
    )
