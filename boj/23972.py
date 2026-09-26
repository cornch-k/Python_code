K, N = map(int, input().split()) #K, N 입력

if N == 1: print(-1) #배율이 1이면 -1 출력

elif (K * N) // (N-1) < 0: print(-1) #(K * N) // (N-1) < 0이면 -1 출력

else:
    if K*N % (N-1) != 0:
        print(K*N // (N-1)+1)
    else:
        print((K * N) // (N-1)) #아니라면 손해는 아니므로 해당 값을 출력