T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    n = [[0]*N for _ in range(N)]
    x, y = 0, 0
    n[x][y] = 1

    #오른쪽, 아래, 왼쪽, 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def turn_left():
        global d
        d = 0
        d += 1
        if d == 4:
            d = 0

    turn_time = 0

    while True:
        turn_left()
        nx = x + dx[d]
        ny = y + dy[d]


        if nx == ny and ny < N and nx < N:
            n[nx][ny] += 1
            x = nx
            y = ny
            turn_time = 0

        else:
            turn_time += 1

        if turn_time == 4:
            nx = x - dx[d]
            ny = y - dy[d]
            if n[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0

        else:
            turn_time += 1
        
        print(n)


    '''
    d_N = 1

    for j in range(N):
        n[0][j] = d_N
        d_N += 1 

    for i in range(1, N):
        n[i][N-1] = d_N
        d_N += 1 
    
    for j in reversed(range(0, N-1)): 
        n[N-1][j] = d_N
        d_N += 1

    for i in reversed(range(1, N-1)):
        n[i][0] = d_N
        d_N += 1

    for j in range(1, N-2):
        n[1][j] = d_N
        d_N += 1

    for i in range(1, N-2):
        n[i][N-2] = d_N
        d_N += 1

    if N-2 != 2:
        for j in reversed(range(2, N-2)): 
            print("j")
            n[N-2][j] = d_N
            d_N += 1        
    else:
        n[N-2][N-2] = d_N
        d_N += 1

        
    print(n)
    '''