n = int(input())
Vote = input()
A = 0
B = 0
for i in range(n):
    if Vote[i] == 'A':
        A += 1
    elif Vote[i] == 'B':
        B += 1

if A > B:
    print("A")
elif B > A:
    print("B")
else:
    print("Tie")