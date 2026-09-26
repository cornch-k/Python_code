a = int(input())

Ascii_pattern = input().split("*")
# *을 기준으로 앞뒤를 나눈다.

first_patteren = Ascii_pattern[0]
second_patteren = Ascii_pattern[1]
# 그렇게 해서 만들어진 앞/뒤

for i in range(a):
    file_name = input()
    #파일 이름

    if first_patteren == file_name[:len(first_patteren)] and second_patteren == file_name[-len(second_patteren):] and len("".join(Ascii_pattern)) <= len(file_name):
        #길다. 롱치즈스틱 스틱 롱!
        #파일 이름의 처음부터 첫 패턴의 길이까지랑 패턴이랑 같고(and) 파일 이름의 두번째 패턴 길이부터 끝까지랑 두 번째 패턴이랑 같고(and) 나누지 않은 패턴의 길이가  파일 이름보다 짧거나 같다면은.
        print("DA")
        #다.
    else:
        print("NE")
        #네.