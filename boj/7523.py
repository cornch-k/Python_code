def sumz(a):
    return a * (a + 1) // 2

def sum(n):
    for i in range(n):
        a, b = map(int, input().split())
        print(f"Scenario #{i+1}:")
        print(sumz(b) - sumz(a-1))
        print()


n = int(input())
sum(n)