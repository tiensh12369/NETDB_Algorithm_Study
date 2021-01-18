T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    add = 0
    sub = 0

    for i in range(1, N+1):
        if i%2 != 0:
            add += i
        else:
            sub -= i
    print("#%d %d" % (test_case,add + sub))