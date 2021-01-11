T = int(input())
for test_case in range(1, T + 1):
    a = 0
    array = list(map(int, input().split(" ")))
    for t in array:
        if t%2 == 1:
            a = a + t
    print ("#%d %d" % (test_case, a))
