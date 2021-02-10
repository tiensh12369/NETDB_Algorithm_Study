import base64
T = int(input())

for test_case in range(1, T + 1):
    de_str = str(base64.b64decode(input()), encoding='utf-8')
    print(f'#{test_case} {de_str}')