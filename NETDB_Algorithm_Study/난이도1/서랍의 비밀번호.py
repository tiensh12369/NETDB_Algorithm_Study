array = list(map(int, input().split(" ")))
P = array[0]
K = array[1]
i = 1

while K < P:
	K += 1
	i += 1
print(i)