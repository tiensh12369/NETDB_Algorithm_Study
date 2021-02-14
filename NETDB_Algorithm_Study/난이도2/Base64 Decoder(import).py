import base64
T = int(input())

for t in range(1, T + 1):
    de_str = str(base64.b64decode(input()), encoding='utf-8')
    print(f'#{t} {de_str}')