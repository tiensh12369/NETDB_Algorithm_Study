T = int(input())

for test_case in range(1, T + 1):
    day = int(input())
    N_case = list(map(int, input().split(" ")))
    
    max_case = 0
    total = 0

    for i in range(day)[::-1]:
        N = N_case[i]
        if N > max_case:
            max_case = N
            continue
        total += (max_case - N)

    print("#{} {}".format(test_case, total))