
import numpy as np

arr1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])

print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

arr2 =arr1.flatten()
print(arr2) 

arr3 =arr2.reshape(3,3)
print(arr3)


print('------------------------------------------')

print('---------Matrix-----------------')

m = np.matrix('1,2,3;4,5,6;7,8,9')
print(m)
print(m.dtype)
print(m.ndim)
print(m.shape)
print(m.size)   

print(np.diagonal(m))

print('------------------------------------------')
print('--------- Matrix Multiplication----------------')

m1 =np.matrix('1,2,3;4,5,6;6,7,8')
m2 = np.matrix('9,8,7;6,5,4;3,2,1')

result =m1 *m2
print(result)