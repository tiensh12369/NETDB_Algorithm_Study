T = int(input())
for i in range(1, T + 1):
    S = input()
    S_list = ["SAT", "FRI", "THU", "WED", "TUE", "MON", "SUN"]
    
    print(f'#{i} {(S_list.index(S)+1)%8}')