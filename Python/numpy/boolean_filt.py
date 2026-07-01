


import numpy as np


arr1=np.array([1,2,3,4,5,6,7,8,9,10])

filt_data=arr1[(arr1>5) & (arr1%2!=0)]

print(arr1)
print(filt_data)


