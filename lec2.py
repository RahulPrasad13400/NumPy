# MULTIDIMENSIONAL ARRAY 
import numpy as np 

array1 = np.array(2)
print(array1)   # 2
print(array1.ndim)  #0

array2 = np.array([2])
print(array2)   # [2]
print(array2.ndim)  # 1

array3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array3)   # [[1,2,3],[4,5,6],[7,8,9]]
print(array3.ndim)  #2
print(array3.shape)

array4 = np.array([[[1,2 ,3],[4, 5, 6],[7, 8, 9]],[[10, 11, 12],[13, 14, 15],[16, 17, 18]],[[19, 20, 21],[22, 23, 24],[25, 26, '']]])
print(array4)
print(array4.ndim)  # 3
print(array4.shape)  # (3, 3, 3)

print(array4[0, 0, 0])  # 1