sum = 1
times = 1

#1 - 1/3 + 1/5
bunmo = 1
while times != 100:
    bunmo +=2
    bunmo *= -1
    sum = sum + (1/bunmo)
    times+= 1
    
print(sum)