T = int(input())
 
for test_case in range(1, T + 1):
    N, K = list(map(int, input().split(" ")))

    count = 0

    while N >= K:
        count += (N%K) + 1
        N = N//K
        
    count += N - 1

    print(f'#{test_case} {count}')