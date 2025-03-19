"""
.ravel() -> view mean it changes original array

.flatten() -> copy mean it create a new array and changes in new array will not reflect in the original array
"""

import numpy as np

arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr_2d.ravel()) #it changes original array to 1d array
print(arr_2d.flatten()) #it create a new 1d array and changes in new array will not reflect in the original array