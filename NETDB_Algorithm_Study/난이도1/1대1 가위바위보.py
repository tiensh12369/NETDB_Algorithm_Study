array = list(map(int, input().split(" ")))

A = array[0]
B = array[1]

if A == 1:
    if B == 2:
        print ("B")
    else:
    	print ("A")
elif A == 2:
    if B == 1:
        print ("A")
    else:
    	print ("B")
elif A == 3:
    if B == 1:
        print ("B")
    else:
    	print ("A")