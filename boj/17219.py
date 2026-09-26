import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

site_password = {}

for i in range(n):
    site, ps = map(str, sys.stdin.readline().rstrip().split())
    site_password[site] = ps

for j in range(m):
    print(site_password[sys.stdin.readline().rstrip()])