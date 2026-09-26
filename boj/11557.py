a = int(input())
for i in range(a):
    list_univ = []
    list_alcohol = []
    b = int(input())
    for j in range(b):
        univ, alcohol = map(str, input().split())
        alcohol = int(alcohol)
        list_univ.append(univ)
        list_alcohol.append(alcohol)
    d = list_alcohol.index(max(list_alcohol))
    print(list_univ[d])