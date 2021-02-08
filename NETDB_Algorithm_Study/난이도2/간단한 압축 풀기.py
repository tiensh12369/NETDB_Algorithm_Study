T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    A = ""
    for n in range(1, N + 1):
        Ci, Ki = list(input().split(" "))
        
        A += Ci * int(Ki)

    print(f'#{test_case}')
    for i in range(len(A)):
        if i%10 == 0 and i != 0:
            print()
        print(A[i], end='')
    print()