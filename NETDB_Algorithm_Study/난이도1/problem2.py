T = int(input())
 
for test_case in range(1, T + 1):
    array = list(map(int, input().split(" ")))
    s = 0
    for i in array:
        s += i
    avg = s/10
    print("#%d %.f" % (test_case, avg))