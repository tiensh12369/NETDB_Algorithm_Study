T = int(input())
for test_case in range(1, T+1):
    P = input().strip()
    Q = input().strip()

    if Q[-1] in 'a' and P == Q[:len(P)] and len(P)+1 == len(Q):
        print(f"#{test_case} N")
    else:
        print(f"#{test_case} Y")
