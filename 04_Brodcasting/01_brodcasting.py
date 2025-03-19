# if i have array or data set i want to apply changes array of different size and shape but loops are very slow in nature so that we use broadcasting for this operation 

# numpy does this work very efficiently and very fast

# example if i want to apply discount on some product prices then

import numpy as np

# operations without broad cast
prices1 = np.array([100,200,300])
discount = 10
final_prices1 = []

for price in prices1:
    result = price - (price * discount / 100)
    final_prices1.append(result)

print(final_prices1)

# this code with broad cast
prices = np.array([100,200,300])
discount = 10 #percent

# here actual broad cast used mean directly performs the operation
final_prices = prices - (prices * discount / 100)

print(final_prices)



