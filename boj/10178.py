a = int(input())
for i in range(a):
    b, c = map(int, input().split())
    print("You get %d piece(s) and your dad gets %d piece(s)." % (b / c, b % c))