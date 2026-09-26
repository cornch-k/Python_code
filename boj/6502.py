i = 1
while 1:
    li = list(map(int, input().split()))
    if li[0] == 0:
        break
    r, w, l = li
    d = (w/2)**2 + (l/2)**2
    if r**2 >= d:
        print("Pizza %d fits on the table." % i)
    else: 
        print("Pizza %d does not fit on the table." % i)
    i += 1