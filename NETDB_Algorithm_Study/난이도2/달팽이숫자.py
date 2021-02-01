T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    n = [[0]*N for _ in range(N)]
    x, y = 0, 0
    count = 1
    n[x][y] = count
    d = 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def turn_right():
        global d
        d += 1
        if d == 4:
            d = -1

    turn_time = 0

    print(f'#{test_case}')
    while count != N**2:
        nx = x + dx[d]
        ny = y + dy[d]
 
        if ny < N and nx < N and n[nx][ny] == 0:
            count += 1
            n[nx][ny] = count
            x = nx
            y = ny

        else:
            nx = x - dx[d]
            ny = y - dy[d]
            turn_right()
    
    for i in range(N):
        print(*n[i])