a =int(input())

Gandalf_score = [1, 2, 3, 3, 4, 10, 0]
Sauron_score = [1, 2, 2, 2, 3, 5, 10]

for i in range(a):
    Gandalf_result = 0
    Sauron_result = 0  
    Gandalf = list(map(int, input().split()))
    Sauron = list(map(int, input().split()))
    Gandalf.append(0)

    for j in range(len(Gandalf)):

        Gandalf[j] *= Gandalf_score[j]
        Sauron[j] *= Sauron_score[j]
        Gandalf_result +=Gandalf[j]
        Sauron_result +=Sauron[j]

    if Gandalf_result > Sauron_result:
        print("Battle %d: Good triumphs over Evil" % (i + 1))
    elif Gandalf_result == Sauron_result:
        print("Battle %d: No victor on this battle field" % (i + 1))
    elif Gandalf_result < Sauron_result:
        print("Battle %d: Evil eradicates all trace of Good" % (i + 1))