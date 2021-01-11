T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
 
for test_case in range(1, T + 1):
    try:
        array = list(map(int, input().split(" ")))
        N = array[0]
        K = array[1]
        i = 0
        while N != 1:
            if N % K == 0:
                N = N/K
            else:
                N = N-1
            i = i+1
    except:
        test_case = test_case+1
 
    print("#%d %d" % (test_case, i))