T = int(input())

for test_case in range(1, T + 1):
    date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d1, day1, d2, day2 = list(map(int, input().split(" ")))

    date = (sum(date[:d2-1]) + day2) - (sum(date[:d1-1]) + day1) + 1
    print(f'#{test_case} {date}')