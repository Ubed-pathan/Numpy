'''
when throw and not throw the error 
1. same shape and size [1,2,3] and [6,7,8] it not throw error 
2. array with single value mean [1,2,3,4] and 3 it not throw error 
3. different shape and size mean [1,2,3] and [[1,2,3],[4,5,6]]
'''

import numpy as np

arr1 = np.array([[1,2,3],[5,6,7]]) #shape is 3 x 3
arr2 = np.array([1,2]) #shape is 1 x 2

# here it cause error becuase shape of array are different
result = arr1 + arr2

print(result)

