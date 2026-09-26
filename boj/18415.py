a = int(input())
b = input()
while True:
    c = b.replace("joi", "JOI")
    if c.find("joi") == -1:
        break
print(c)