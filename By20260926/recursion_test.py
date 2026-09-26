def countdown(n):
    if n == 0:
        return "Blast Off!"
    else:
        print(n)
        countdown(n-1)

a = int(input("원하는 숫자를 입력해주세요.\n입력하신 숫자로 카운트다운을 시작합니다.\n>> "))
countdown(a)