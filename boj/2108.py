# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이 (max-min)


def sansul(n:list):
    return sum(n) // len(n)

def chungang(n:list):
    n.sort()
    return n[len(n) // 2]

def choebin(n:list):
    d = {}
    for i in n:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    m = max(d.values())
    for k, v in d.items():
        if v == m:
            return k

def max_min_difference(n:list):
    return max(n) - min(n)


n = int(input())
list = []
for i in range(n):
    list.append(int(input()))

print(f"{sansul(list)}\n{chungang(list)}\n{choebin(list)}\n{max_min_difference(list)}")