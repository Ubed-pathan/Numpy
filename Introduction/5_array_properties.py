import numpy as np

array = [
    [1, 2, 3],
    [4, 5, 6]
]

# this is below function return us the size of array and number of elements in it
print(np.shape(array)) # (2, 3) 2 rows and 3 columns and 6 elements in total
print(np.size(array)) # 6

# this is method helps to fng the diamention of array
print(np.ndim(array)) # 2

# this is method helps to find the data type of array
print(np.dtype(array)) # int32

# it helps to convert the data type of array
print(array.astype(float)) # [[1. 2. 3.]
