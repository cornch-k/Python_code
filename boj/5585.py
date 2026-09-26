money = [500, 100, 50, 10, 5, 1]

n = int(input())
gsr = 1000 - n

counter = 0
whilecount = 0
while gsr != 0:
    if gsr // money[whilecount] >= 1:
        gsr -= (gsr // money[whilecount])
        counter += (gsr // money[whilecount])
        whilecount += 1
print(counter)