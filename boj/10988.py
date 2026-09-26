def kaibun():
    a = list(str(input()))
    b = list(reversed(a))
    if a == b:
        return 1
    else:
        return 0
print(kaibun())