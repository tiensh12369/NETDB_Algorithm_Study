T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    n = [[0]*N for _ in range(N)]
    x, y = 0, 0
    n[x][y] = 1
    d = -1
    #오른쪽, 아래, 왼쪽, 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def turn_right():
        global d
        d += 1
        if d == 4:
            d = -1

    turn_time = 0

    while True:
        turn_right()
        nx = x + dx[d]
        ny = y + dy[d]
        print(nx, ny)

        if nx != ny and ny < N and nx < N:
            n[nx][ny] = 1
            x = nx
            y = ny
            turn_time = 0
            print(x, y)

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