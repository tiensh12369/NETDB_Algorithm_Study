N = int(input())

string_num = []

for num in range(1, N + 1):

    three = str(num).count("3")
    six = str(num).count("6")
    nine = str(num).count("9")

    count_369 = three + six + nine

    if count_369 > 0:
        for count in range(count_369):
            print("-", end ="")
        print(" ", end="")

    else:
        print(num, end=" ")