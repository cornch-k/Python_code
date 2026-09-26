chapter = [] #각 챕터의 공부시간

limit_time = 30 #제한시간
half = 0 #시간 절반 확인용도, 초기화.
result = 0 #답 출력용도

n = int(input())

for i in range(n):
    time = int(input())
    chapter.append(time)

for j in range(n):
    if limit_time <= 0:  #제한시간이 0보다 작거나 같으면 즉, 시간이 없다면 보충
        limit_time = 30

    half = chapter[j] / 2 #챕터시간 절반으로 만들기

    if limit_time - chapter[j] >=0: #챕터를 끝내고 시간이 남는 경우
        limit_time = limit_time - chapter[j]
        result += 1

    elif limit_time - chapter[j] <= 0 and limit_time >= half: #챕터를 끝내지 못했지만, 공부한 시간이 절반을 넘을 경우
        limit_time = 0
        result += 1

    elif limit_time - chapter[j] <= 0 and limit_time < half: #챕터를 끝내지 못했고, 공부한 시간이 절반을 넘기지 못한 경우
        limit_time = 0
        continue

print(result)