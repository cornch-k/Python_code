height = list()
for i in range(9):
    a = int(input()); height.append(a)

heightsum = sum(height)
for i in range(9):
    for j in range(i+1, 9):
        if heightsum - (height[i] + height[j]) == 100:
            num1, num2 = height[i], height[j]
            height.remove(num1)
            height.remove(num2)
            height.sort()

            for i in range(len(height)):
                print(height[i])
            break

    if len(height) < 9:
        break