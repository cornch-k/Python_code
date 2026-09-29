D = int(input())
N = int(input())
Attendance_list = [0] * (D + 2)
# print(Attendance_list)

for i in range(N):
    L, R = map(int, input().split())
    Attendance_list[L] += 1
    Attendance_list[R + 1] -= 1

Attendance_list_PS = [0]
for i in range(1, D + 1):
    Attendance_list_PS.append(Attendance_list_PS[i - 1] + Attendance_list[i])


for i in range(1, D + 1):
    print(Attendance_list_PS[i])
