'''
T = int(input())
c = (50000, 10000, 5000, 1000, 500, 100, 50, 10)
d = [0]*len(c)

for test_case in range(1, T + 1):
	money = int(input())
    
	print(f'#{test_case}')

          
	for i in range(len(c)):
		d[i] = money // c[i]
		money = money % c[i]
		print(d[i], end=" ")
          
	print()
'''

T = int(input())

for test_case in range(1, T + 1):
	input_T = int(input())
	don = (50000, 10000, 5000, 1000, 500, 100, 50, 10)
	cont = 0
	i = 0
	cont_n = []
    
	print("#%d" % (test_case))
    
	while i < len(don):

		if input_T >= don[i]:
			input_T = input_T - don[i]
			cont += 1

		else:
			cont_n.append(cont)
			cont = 0
			print(cont_n[i], end = " ")
			i += 1
	print()