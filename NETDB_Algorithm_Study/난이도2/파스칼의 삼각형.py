T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    a = [1] 
    c = []

    print("#%d" % test_case)
    print(a[0])
    

    for i in range(N-1):
        a.append(0) 
        b = []
        for item in a[::-1]:
            b.append(item)

        for i in range(len(a)):
            c.append(a[i] + b[i])

        d = " ".join(map(str, c[:]))	
        print(d)
        a = c
        c = []