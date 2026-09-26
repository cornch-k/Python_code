def infp():
    check = 'Happy'

    n = int(input())
    cloth_list = list(map(int, input().split())) # [1, 5, 4, 1, 2] 리스트 생성

    check_cloth = int(sum(cloth_list) / 2) # [인원수 / 2]
    
    for i in range(len(cloth_list)): 
        if check_cloth < cloth_list[i]:
            if n == 1:
                if cloth_list[i] == 1:
                    continue
                else:
                    check = 'Unhappy'
                    break
            else:
                check = 'Unhappy'
    return check

print(infp())

