a = int(input())

for i in range(a):

    life = input()
    result = 0

    for j in life:
        if j == " ":
            continue
        else:
            alpha_score = ord(j) - 64
            result += alpha_score

    if result == 100:
        print("PERFECT LIFE")
    else:
        print(result)