def bin_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0


a = int(input())
b = list(map(int, input().split())); b.sort()
c = int(input())
d = list(map(int, input().split()))


for i in range(len(d)):
    print(bin_search(b, d[i]))