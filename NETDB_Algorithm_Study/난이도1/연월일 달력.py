T = int(input())

for test_case in range(1, T + 1):
	array = []
	for i in input():
		array.append(i)

	yyyy = "".join(map(str, array[0:4]))
	mm = "".join(map(str, array[4:6]))
	dd = "".join(map(str, array[6:8]))

	print("#%d" % (test_case), end=" ")
    
	if int(mm) == 1 or int(mm) == 3 or int(mm) == 5 or int(mm) == 7 or int(mm) == 8 or int(mm) == 10 or int(mm) == 12:
		if 1 <= int(dd) <= 31:
			print("%s/%s/%s" % (yyyy,mm,dd))
		else:
			print("-1")

	elif int(mm) == 4 or int(mm) == 6 or int(mm) == 9 or int(mm) == 11:
		if 1 <= int(dd) <= 30:
			print("%s/%s/%s" % (yyyy,mm,dd))
		else:
			print("-1")

	elif int(mm) == 2:
		if 1 <= int(dd) <= 28:
			print("%s/%s/%s" % (yyyy,mm,dd))
		else:
			print("-1")
	else:
		print("-1")