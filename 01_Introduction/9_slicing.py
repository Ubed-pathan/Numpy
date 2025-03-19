# slicing mean perticular portion of array is extracted
#
# syntax of slicing is array_name[start:stop:step]
#
# start :- it is the starting index of the array
# stop :- it is the ending index of the array
# step :- it is the difference between the index
#
# if we don't provide the start, stop and step then by default it will take the start as 0, stop as length of array and step as 1   
#
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

print(arr[0:]) # [ 1  2  3  4  5  6  7  8  9 10]
print(arr[:]) # [ 1  2  3  4  5  6  7  8  9 10]
print(arr[:5]) # [1 2 3 4 5]
print(arr[0:5]) # [1 2 3 4 5]
print(arr[0:5:2]) # [1 3 5] 
print(arr[0:5:3]) # [1 4]
print(arr[0:5:4]) # [1 5]
print(arr[::-1]) # [10  9  8  7  6  5  4  3  2  1]
print(arr[::-2]) # [10  8  6  4  2]
print(arr[::-3]) # [10  7  4  1]
