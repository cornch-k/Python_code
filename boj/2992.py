import itertools

a = list(input())

arr_a = list(itertools.permutations(a, len(a)))
arr_a.sort(reverse=True)

result = []
for i in arr_a: # arr에서 값을 가져오기
    result.append("".join(i)) # 튜플을 문자열로 합침

idx = result.index("".join(a)) # 숫자가 있는 인덱스 번호를 찾기
print(result[idx-1] if idx != 0 else 0) # 제일 큰 수가 아니라면 현재보다 바로 큰 값을 출력하고 0을 출력한다.

