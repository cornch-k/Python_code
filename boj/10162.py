def time(second) ->int:
    if second % 10 != 0:
        print(-1)
    else:
        divide(second)


def divide(time) -> int:
    five_min = 0
    one_min = 0
    ten_sec = 0
    while time != 0:
        if time - 300 >= 0:
            time -= 300; five_min += 1
        elif time - 60 >= 0:
            time -= 60; one_min += 1
        elif time - 10 >= 0:
            time -= 10; ten_sec +=1
    print(f"{five_min} {one_min} {ten_sec}")

a = int(input()) # 시간 입력
time(a)