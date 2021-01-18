T = int(input())

for test_case in range(1, T + 1):
    word = list(input())
    palindrome = []

    for item in word[::-1]:
        palindrome.append(item)

    if word == palindrome:
        print("#%d 1" % test_case)
    else:
        print("#%d 0" % test_case)