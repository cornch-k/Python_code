def solve(a):
    n = len(a)
    for i in range(1, n):
        if a[i-1] > a[i]:
            return False
    return True

a = list(map(int, input().split()))
if solve(a):
    print("Good")
else:
    print("Bad")