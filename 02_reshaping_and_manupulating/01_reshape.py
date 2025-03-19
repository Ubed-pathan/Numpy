"""
Reshaping

reshape(row, column) - reshapes the array to the given row and column
if dimension is not same then it will give error

"""

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

# it not create a new array it just change the shape of the array
# it mean it showing view of the array
# changes in new array will reflect in the original array

print(arr.reshape(2,5)) # [[ 1  2  3  4  5]
                        #  [ 6  7  8  9 10]]
print(arr.reshape(5,2)) # [[ 1  2]
                        #  [ 3  4]
                        #  [ 5  6]
                        #  [ 7  8]
                        #  [ 9 10]] 