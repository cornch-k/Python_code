N, M = map(int, input().split())
result = str(N) * N
if len(result) > M:
    print(result[:M])
else:
    print(result)