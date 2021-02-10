T = int(input())

for test_case in range(1, T+1):
    num_T = int(input())
    dist = list(map(int, input().strip().split(" ")))
    count={}
    for i in dist:
        try:
            count[i] += 1
        except:
            count[i] = 1
    key_max = max(count.keys(), key=(lambda k: count[k]))
    print(f'#{test_case} {key_max}')