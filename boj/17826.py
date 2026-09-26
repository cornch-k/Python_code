import sys

hakjeom = 0

grade_list = list(map(int, sys.stdin.readline().split()))
hongik = int(sys.stdin.readline())

hakjeom = (grade_list.index(hongik) + 1)

if  1 <= hakjeom <= 5:
    print("A+")
elif 6 <= hakjeom <= 15:
    print("A0")
elif 16 <= hakjeom <= 30:
    print("B+")
elif 31 <= hakjeom <= 35:
    print("B0")
elif 36 <= hakjeom <= 45:
    print("C+")
elif 46 <= hakjeom <= 48:
    print("C0")
else:
    print("F")