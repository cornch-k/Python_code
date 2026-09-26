input_words = input().upper()
word_list = list(set(input_words))
cnt = []

for i in word_list:
    count = input_words.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[cnt.index(max(cnt))])