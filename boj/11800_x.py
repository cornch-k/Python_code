n = int(input())
name = [0, "Yakk", "Doh", "Seh", "Ghar", "Bang", "Sheesh"]

for i in range(n):
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    print("Case %d: " %(i+1), end="")
    if l[0] == l[1] == 1:
        print("Habb Yakk")
    elif l[0] == l[1] == 2:
        print("Dobara")
    elif l[0] == l[1] == 3:
        print("Dousa")
    elif l[0] == l[1] == 4:
        print("Dorgy")
    elif l[0] == l[1] == 5:
        print("Dabash")
    elif l[0] == l[1] == 6:
        print("Dosh")
    elif l[0] == 6 and l[1] == 5:
        print("Sheesh Beesh")
    else:
        print(name[l[0]], name[l[1]])