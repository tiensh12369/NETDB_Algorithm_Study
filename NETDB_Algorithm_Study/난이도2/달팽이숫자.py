T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    n = []
    for i in range(1, N**2+1):
        n.append(i)
    
    

    '''
    print(n[:N])
    print(n[N+N+1:], n[N])
    print(n[N+N:N:-1])

    1,2,3,4,5,6,7,8,9

    N = 4

    0 1 2 N

    print(n[0], n[1], n[2])
    print(n[7], n[8], n[3])
    print(n[6], n[5], n[4])
    '''

    print(n[:N])
    print(n[N+N+3:N+N+N+2], n[N])
    print(n[N+N+2],n[:N+N+N+1:-1], n[N+1])
    print(n[N+N+1:N+1:-1])
