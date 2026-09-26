A= list(map(int,input().split()))

B = (A[2]-A[1])/(A[0]-A[1])

print(int(B) if B == int(B) else int(B)+1)