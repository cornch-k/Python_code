N, Q = map(int, input().split())
A = list(map(int, input().split()))
prefixSum_A = list()
prefixSum_A.append(A[0])
for i in range(1, N):
    prefixSum_A.append(prefixSum_A[i - 1] + A[i])

for i in range(Q):
    L, R = map(int, input().split())
    print(prefixSum_A[R - 1] - prefixSum_A[L - 1] + A[L - 1])
