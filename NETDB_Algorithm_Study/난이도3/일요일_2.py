T = int(input())
for i in range(1, T + 1):
    S = input()
    S_dict = {"SAT":1, "FRI":2, "THU":3, "WED":4, "TUE":5, "MON":6, "SUN":7}
    
    print(f'#{i} {S_dict[S]}')