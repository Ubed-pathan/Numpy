# fancy indexing
# fancy indexing is a technique in which we pass an array of
# indices in place of single index to access multiple elements of the array
#
# syntax of fancy indexing is array_name[array_of_indices]
#
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

# it make a new array of elements at index 0,1,2 but not change the original array
print(arr[[0,1,2]]) # [1 2 3]
print(arr[[0,3,5]]) # [1 4 6]
print(arr[[0,2,4]]) # [1 3 5]