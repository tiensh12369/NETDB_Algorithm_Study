N = int(input())

for num in range(1, N + 1):
    count_369 = 0

    for count in '369':
        count_369 += str(num).count(count)
    if count_369 > 0:
        print("-"*count_369, end =" ")
    else:
        print(num, end=" ")

'''
N = int(input())
for num in range(1, N + 1):
    count_369 = sum(str(num).count(count) for count in '369')
    print("-"*count_369, end=" ") if count_369>0 else print(num, end=" ")
'''