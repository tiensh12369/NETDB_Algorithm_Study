T = int(input())

for test_case in range(1, T + 1):
    array = []
    left_sum, right_sum = 0, 0

    for N in input():
        array.append(N)

    even = int(len(array)/2)

    if len(array)%2 == 0:
        left_sum = sum(map(int, (array[:even])))
        right_sum = sum(map(int, (array[even:])))

    print(f'#{test_case}', end=" ")

    if left_sum == right_sum:
        print("LUCKY")
    else:
        print("READY")