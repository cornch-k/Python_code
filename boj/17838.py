n = int(input())
for i in range(n):
    command = input()
    command_list = list()
    for i in range(len(command)):
        command_list.append(command[i])
    if len(command_list) != 7:
        print(0)
    else:
        if command_list[0] == command_list[1] == command_list[4] and command_list[2] == command_list[3] == command_list[5] == command_list[6] and command_list[0] != command_list[2]:
            print(1)
        else:
            print(0)