T = int(input())

for test_case in range(1, T + 1):
    h1, m1, h2, m2 = list(map(int, input().split(" ")))

    h = h1 + h2
    m = m1 + m2

    if h > 12:
        h -= 12
    elif h < 1:
        h += 12
    
    if m > 59:
        m -= 60
        h += 1
    elif m < 0:
        m += 60

    print(f'#{test_case} {h} {m}')