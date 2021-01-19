import math

T = int(input())

for test_case in range(1, T + 1):
    (N, K) = list(map(int, input().split(" ")))
    credit = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    total = []

    for i in range(N):
        (midex, finalex, task) = list(map(int, input().split(" ")))
        total.append(midex*0.35 + finalex*0.45 + task*0.2)
        #print(total[i])

    totalsort = sorted(total, reverse = True)

    print(f'#{test_case} {credit[math.trunc(totalsort.index(total[K-1]) * (len(credit)/N))]}')