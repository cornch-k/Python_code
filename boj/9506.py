while True:
    a = int(input())
    if a == -1:
        break
    else:
        count = 0
        list = []
        for i in range(1, a): # 1 ~ a까지
            if a % i == 0: # 만약 a % i == 0 이라면 
                list.append(str(i))
                count += i
        if a > count or a < count:
            print(f"{a} is NOT perfect.")
        else:
            print(f"{a} = ", end = "")
            print(" + ".join(list))