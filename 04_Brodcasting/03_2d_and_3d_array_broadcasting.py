import numpy as np 

matrix = np.array([[1,2,3],[4,5,6]])
# vector is nothing but 1d array
vector = np.array([10,20,30])

# what actually broad casting did here every single element in one diamensional array added with every element in two dimensional array
result = matrix + vector

print(result)