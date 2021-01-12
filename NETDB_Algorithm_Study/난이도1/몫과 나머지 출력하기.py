import math
T = int(input())

for test_case in range(1, T + 1):
    array = list(map(int, input().split(" ")))
    P = array[0]
    K = array[1]

    share = math.floor(P/K)
    remainder = P%K

    print("#%d %d %d" % (test_case, share, remainder))