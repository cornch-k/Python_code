A = int(input())
B = int(input())
C = int(input())
if A + B + C != 180:
    print("Error")
elif A == B == C == 60:
    print("Equilateral")
elif A + B + C == 180 and A == B or A == C or B == C:
    print("Isosceles")
elif A + B + C == 180 and A != B != C:
    print("Scalene")