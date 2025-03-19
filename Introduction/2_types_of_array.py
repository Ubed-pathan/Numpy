import numpy as np;

# this is for one dimensional array
default_array = np.zeros(5)
print(default_array)

# this is for two dimensional array
default_array = np.zeros((5, 3))
print(default_array)

# i can use one instead of zeros 
default_array = np.ones(5)
print(default_array)

# i can use any number as default value in array
default_array = np.full((3,3),4)
print(default_array)