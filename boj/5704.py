import sys

while True:
    a = input()
    
    if a == "*":
        break

    else:
        for i in range(97, 123):
            if a.find(chr(i)) == -1:
                print('N')
                break
    
    print('Y')