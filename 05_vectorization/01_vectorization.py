# it mean apply operation on entire array in once without using loop
# vectorization is very fast than loop

# example without vectorization
list1=[1,2,3]
list2=[4,5,6]
# it work but very slow
result = [x+y for x,y in zip(list1,list2)]
print(result)

# example with vectorization
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result = arr1 + arr2
# it is very fast than loop
print(result)

# vectorization mulipliation
result = arr1 * arr2
print(result)

# vectorization division
# here it divedes every element of arr1 by 2
result = arr1 / 2
print(result)

# difference between broadcasting and vectorization
# broadcasting expands the smaller array to match the shape of the larger array
# faster than loop
# it is used in 1D to 2D expands

# vectrorization apply operation on entire array in once without using loop
# faster than broadcasting
# it is very fast than loop mean 100x times faster than loop
# it is used in matrix operation