n = int(input())
for i in range(n):
    a, b = input().split()
    a_list = list(a)
    b_list = list(b)
    a_list.sort()
    b_list.sort()
    if a_list == b_list:
        print("%s & %s are anagrams." %(a, b))
    else:
        print("%s & %s are NOT anagrams." %(a, b))
