a = int(input())

for i in range(a):
    b, c =  map(str, input().split())
    b = int(b)
    
    print(c[:b-1], c[b:], sep='')