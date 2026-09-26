from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) ->int:
    
    pl = 0 #검색범위 맨 앞 인덱스
    pr = len(a)-1 #검색범위 맨 뒤 인덱스

    while True:
        pc = (pl + pr) // 2 #검색범위 중앙 인덱스
        if a[pc] == key: #중앙값이 key값이라 검색에 성공했다면, pc값을 출력
            return pc 

        elif a[pc] < key: #key값이 중앙값보다 크다면, 뒤쪽 절반으로 검색범위를 좁힘
            pl = pc + 1

        else: #key값이 중앙값보다 작다면, 앞쪽 절반으로 검색범위를 좁힘
            pr = pc - 1
            
        if pl > pc: #검색 실패시 
            break
    return -1

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num

    print('배열 데이터를 오름차순으로 입력하세요: ')
    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i-1]:
                break
    
    ky = int(input('검색할 값을 입력하세요: '))

    idx = bin_search(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소를 찾지 못했습니다.')
    else:
        print(f'검색값은 x[{i}]에 있습니다.')