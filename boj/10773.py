def for_stack(n):
    stack = list()

    for i in range(n):
        num = int(input())

        if num == 0: stack.pop()
        else: stack.append(num)

    print(sum(stack))

a = int(input())
for_stack(a)