# when we work on real time project we will work on misssing values
# we have to hndle missing data 
# also the mathematical error like divide by zero

# numpy helps to handle missing values
# there are some built in functions in numpy to handle missing values
# 1. isnan()  it mean not a number : to check or detect missing values
# it checks any missing value in array and return boolean value
# 2. nan_to_num() : to replace missing values with zero
# 3. isfinite() or isinf: to check or detect finite values 

import numpy as np

# examples of isnan()
arr = np.array([1,2,np.nan,4,np.nan, 6])
# true means missing values
# false means no missing values
print(np.isnan(arr)) # [False False  True False  True False]

# interview question so answer of this question is we cant compare nan with nan
# it will return False
print(np.nan == np.nan)

# if we want to replace missing values of nan then it is possible by nan_to_num()
# examples of nan_to_num()
arr = np.array([1,2,np.nan,4,np.nan, 6])
# here missing values are replaced by zero
print(np.nan_to_num(arr)) # [1. 2. 0. 4. 0. 6.]

# if we want to value replace by any other value then we can do this by passing value in nan_to_num()
print(np.nan_to_num(arr, nan = 100)) # [  1.   2. 100.   4. 100.   6.]


# if we want to handle finite numbers
# like 10^1000 it will give large number 
# 1/0 it leads to infinite 
# we can handle it by np.isinf
# it returns boolean values

arr = np.array([1,2,np.inf,4,-np.inf,6])
# if infinite value present then true else false
print(np.isinf(arr))

# how to replace infinite values then use nan_to_num
# posinf = positive infinite
# neginf = negative infinite
print(np.nan_to_num(arr, posinf=1000, neginf=1000))


