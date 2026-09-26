import sys
n = int(sys.stdin.readline())

obj_list = list(map(int, sys.stdin.readline().split()))
obj_list.sort()
print(obj_list[-1])