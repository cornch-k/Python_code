
N, W, H, L = map(int, input().split())
W //= L
H //= L
result = W * H
if result > N:
    print(N)
else:
    print(result)