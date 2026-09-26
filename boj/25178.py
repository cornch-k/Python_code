n = int(input())

a_str = input() # 첫번째 문자열
b_str = input() # 두번째 문자열

a_vowel = a_str
b_vowel = b_str

a_list = list()
b_list = list()

vowel = ('a', 'i', 'u', 'e', 'o')

check_list = True

for i in a_str:
    a_list.append(i)

for i in b_str:
    b_list.append(i)

a_list.sort()
b_list.sort()

for j in range(len(a_list)):
    if a_list[j] != b_list[j]:
        check_list = False
        break




for i in a_str:
    if i in vowel:
        a_vowel = a_vowel.replace(i, "")

for i in b_str:
    if i in vowel:
        b_vowel = b_vowel.replace(i, "")

if a_str[0] == b_str[0] and a_str[-1] == b_str[-1] and a_vowel == b_vowel and check_list:
    print("YES")
else:
    print("NO")