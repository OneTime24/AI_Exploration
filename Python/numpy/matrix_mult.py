


import numpy as np


arr1=np.array([[1,2,3],         #2/3
              [4,5,6]])

arr2=np.array([[1,1],
               [2,2],
               [3,3]])          #3/2


print(arr1*arr2)

print(arr1@arr2)

print(np.dot(arr1,arr2))


print(arr2.T)
