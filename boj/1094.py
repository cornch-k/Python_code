count = 0
stick = 64
a = int(input())

while True:
    if a == stick: #만약 스틱이랑 입력이랑 같다면
        count +=1 #1 추가
        break
    else: #스틱이랑 다르다면
        stick = stick / 2 #스틱 2로 나누기
        if stick < a:
            count +=1
            a = a - stick

print(count)