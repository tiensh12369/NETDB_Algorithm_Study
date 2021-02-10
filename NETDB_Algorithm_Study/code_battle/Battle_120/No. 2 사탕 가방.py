T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split(" ")))
    conut_N = list(map(int, input().split(" ")))
    s = []

    for i in conut_N:
        s.append(i/round(i/sum(conut_N, 2)*M))
    print(f"#{test_case} {round(min(s))}")