T = int(input())
 
for test_case in range(1, T + 1):
    array = list(map(int, input().split(" ")))
     
    if array[0] < array[1]:
        print("#%d <" % (test_case))
    elif array[0] > array[1]:
        print("#%d >" % (test_case))
    else:
        print("#%d =" % (test_case))