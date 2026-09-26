while True:
    s = input()
    if s == '#': break

    x = -1
    for i in range(len(s)):
        if s[i] in ['a', 'e', 'i', 'o', 'u']:
            x = i
            break
    
    if x != -1:print(s[x:] + s[:x] + 'ay')
    else: print(s + 'ay')