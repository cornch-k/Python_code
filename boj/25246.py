word = input()
if word[-1] == 'n':
    print(word + 'ry')
elif word[-1] == 'a' or word[-1] == 'e' or word[-1] == 'i' or word[-1] == 'o' or word[-1] == 'u':
    print(word + 'ntry')
elif word[-2] == 'a' or word[-2] == 'e' or word[-2] == 'i' or word[-2] == 'o' or word[-2] == 'u':
    print(word[:-1] + 'ntry')