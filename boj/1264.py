while True:
    count_vowels = 0
    a = input()
    if a == '#':
        break
    else:
        count_vowels += a.count('a')
        count_vowels += a.count('i')
        count_vowels += a.count('u')
        count_vowels += a.count('e')
        count_vowels += a.count('o')
        count_vowels += a.count('A')
        count_vowels += a.count('I')
        count_vowels += a.count('U')
        count_vowels += a.count('E')
        count_vowels += a.count('O')
    print(count_vowels)