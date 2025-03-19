# index is used to access the single elements of the array
#
# slicing is used to access the multiple elements of the array

# indexing in which there are two types of indexing
# 1. positive indexing
# 2. negative indexing

# positive indexing :- it is used to access the elements from the start of the array
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

print(arr[0]) # 1
print(arr[1]) # 2 
print(arr[2]) # 3

# negative indexing :- it is used to access the elements from the end of the array
print(arr[-1]) # 10
print(arr[-2]) # 9
print(arr[-3]) # 8
