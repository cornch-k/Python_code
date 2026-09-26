from lib2to3.pgen2.token import RPAR


R1, S = map(int, input().split())
R2 = 0
S = S * 2
R2 = S - R1
print(R2)