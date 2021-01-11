import math
 
T = int(input())
 
array = list(map(int, input().split(" ")))
array.sort()
 
mid = math.ceil(len(array)/2-1)
 
print (array[mid])