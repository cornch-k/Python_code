a = input()
count_JOI = 0
count_IOI = 0


for i in range(len(a) - 2):
    JOI = "JOI"
    IOI = "IOI"
    string_input  = ""
    string_input += a[i] + a[i+1] + a[i+2]

    if JOI == string_input:
        count_JOI +=1
    elif IOI == string_input:
        count_IOI += 1


print("%d\n%d" %(count_JOI, count_IOI))