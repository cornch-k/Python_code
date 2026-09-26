input_list = list(map(str, input().split()))

# 2 + 4 = 6 => YES
# 2 + 4 + 5 =>NO

a = int(input_list[0])
b = int(input_list[2])
c = int(input_list[4])
if a + b == c:
    print("YES")
else:
    print("NO")