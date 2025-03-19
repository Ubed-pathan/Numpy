"""
numpy.insert(arr,index,value. axis=None);
# arr mean original array
# index mean index at which value is to be inserted
# value mean value to be inserted
# axis mean axis along which value is to be inserted
# if axis is not given then it will insert in 1d array
if axis 0 mean row wise insertion
if axis 1 mean column wise insertion
numpy.delete(arr,index);
numpy.unique(arr);
numpy.concatenate((arr1,arr2));
numpy.vstack((arr1,arr2));
numpy.hstack((arr1,arr2));
numpy.column_stack((arr1,arr2));
numpy.row_stack((arr1,arr2));
numpy.split(arr,index);
numpy.hsplit(arr,index);
numpy.vsplit(arr,index);
numpy.array_split(arr,index);
numpy.append(arr,value);
numpy.sort(arr);
numpy.argsort(arr);
numpy.argmax(arr);
numpy.argmin(arr);
numpy.where(condition);
numpy.extract(condition,arr);
numpy.nonzero(arr);
numpy.searchsorted(arr,value);
numpy.resize(arr,size);
numpy.trim_zeros(arr);
numpy.flip(arr);
numpy.fliplr(arr);
numpy.flipud(arr);
numpy.roll(arr,shift); 
numpy.rot90(arr);
numpy.swapaxes(arr,axis1,axis2);
numpy.transpose(arr);
numpy.moveaxis(arr,axis1,axis2);
numpy.rollaxis(arr,axis,shift);
numpy.ravel(arr);
numpy.flatten(arr);
numpy.squeeze(arr);
numpy.broadcast_to(arr,shape);
numpy.broadcast_arrays(arr1,arr2);
numpy.expand_dims(arr,axis);
numpy.squeeze(arr,axis);
numpy.broadcast_to(arr,shape); 
numpy.broadcast_arrays(arr1,arr2);
numpy.expand_dims(arr,axis);
numpy.squeeze(arr,axis);
numpy.broadcast_to(arr,shape);
numpy.broadcast_arrays(arr1,arr2);
numpy.expand_dims(arr,axis);
numpy.squeeze(arr,axis);
numpy.broadcast_to(arr,shape);
numpy.broadcast_arrays(arr1,arr2);
numpy.expand_dims(arr,axis);
numpy.squeeze(arr,axis);
numpy.broadcast_to(arr,shape);
"""

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr) # [ 1  2  3  4  5  6  7  8  9 10]

# insert
print(np.insert(arr,5,100)) # [  1   2   3   4   5 100   6   7   8   9  10]
print(np.insert(arr,5,100,axis=0)) # [  1   2   3   4   5 100   6   7   8   9  10]
arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])   
print(np.insert(arr_2d,1,100,axis=0)) # [[  1   2   3   4]
                                       #  [100 100 100 100]
                                       #  [  5   6   7   8]
                                       #  [  9  10  11  12]]
print(np.insert(arr_2d,3,[100,200,300,400],axis=0)) # [[  1   2   3   4] 
                                                    #  [  5   6   7   8]
                                                    #  [  9  10  11  12]
                                                    #  [100 200 300 400]]                                       
print(np.insert(arr_2d,1,100,axis=1)) # [[  1 100   2   3   4]
                                        #  [  5 100   6   7   8]
                                        #  [  9 100  10  11  12]]   

# append
print(np.append(arr,100)) # [  1   2   3   4   5   6   7   8   9  10 100]
# it insert value at the end of the array
print(np.append(arr,[100,200,300])) # [  1   2   3   4   5   6   7   8   9  10 100 200 300]
arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(np.append(arr_2d,[[100,200,300,400]],axis=0)) # [[  1   2   3   4]
                                                    #  [  5   6   7   8]
                                                    #  [  9  10  11  12]
                                                    #  [100 200 300 400]]

# insert in numpy add the element at any specific index 
print(np.insert(arr, 0, 100))


# concatenate in numpy merge the two arrays
# in this axis 0 = vertical stacking
#  axis 1 = horizontal stacking
arr10 = [1,2,3,4,5]
arr11 = [3,4,5,7,6]

arr12 = [8,7,6]
arr13 = [3,6,7]

print(np.concatenate((arr10, arr11)))

# delete in numpy removes the element from specific index like 
# it accept three argument np.delete(array, index, axis = None)

arr = [1,2,3,4]
# here arr is python list and when i am using this arr in delete it will automatically converted to array
print(np.delete(arr, 3))

arr_2d = [[1,2,3],[4,5,6]]
# here o mean delete inex of row and axis=0 mean delete row wise
print(np.delete(arr_2d, 0, axis = 0))


"""
    vertically and horizontally 
    vstack() row wise 
    hstack() column wise
"""

arr1 = [1,2,3]
arr2 = [4,5,6]

print(np.vstack((arr1, arr2)))
print(np.hstack((arr1, arr2)))



'''
spliting in array is diving array into the parts 
there are 3 methods in spliting 

equal 
np.hsplit() 
np.vsplit() 

'''

arr22 =np.array([1,2,3,4,5,6])
#  it not conert array to list directly
print(np.split(arr22,2))