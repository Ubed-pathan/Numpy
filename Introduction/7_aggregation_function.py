import numpy as np

array = [1,2,3,4]

print(np.sum(array)) # 10
print(np.prod(array)) # 24
print(np.mean(array)) # 2.5
print(np.std(array)) # 1.118033988749895
print(np.var(array)) # 1.25
print(np.min(array)) # 1
print(np.max(array)) # 4
print(np.argmin(array)) # 0
print(np.argmax(array)) # 3
print(np.median(array)) # 2.5
print(np.percentile(array, 25)) # 1.75
print(np.any(array)) # True
print(np.all(array)) # True
print(np.unique(array)) # [1 2 3 4]
print(np.sort(array)) # [1 2 3 4]
print(np.argsort(array)) # [0 1 2 3]
print(np.argwhere(array)) # [[1]