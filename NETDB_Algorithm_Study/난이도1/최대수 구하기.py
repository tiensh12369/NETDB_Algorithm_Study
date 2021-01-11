T = int(input())
 
for test_case in range(1, T+1):
    array = list(map(int, input().split(" ")))
    big = max(array)
         
    print ("#%d %d" % (test_case, big)) 