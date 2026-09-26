import sys
n = int(sys.stdin.readline())

log_list = set()

for i in range(n):
    name, log = map(str, sys.stdin.readline().split())
    if log == "enter":
        log_list.add(name)
    if log == "leave":
        log_list.remove(name)

for j in sorted(log_list, reverse=True):
    print(j)