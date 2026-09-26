import sys
n = int(sys.stdin.readline())

for i in range(n):

    string = input()
    counting = len(string)

    if counting == 1:
        print(string * 2)
    else:
        print("%s%s" %(string[0], string[-1]))