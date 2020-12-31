import numpy as np

'''view Example :- Board casting hoti h es me'''
arr = np.array([5,10,15])

arr_slice= arr[0:2]

# print(arr_slice) #[5,10]

arr_slice[:]= 0

# print(arr_slice) #[0,0]

# print(arr) #[0,0,15]

'''Copy Example :- Board casting hoti h es me'''

arr_copy = np.array([5,10,15])
arr_slice2= arr_copy[0:2].copy()
print(arr_slice2) #[5,10]

arr_slice2[:]=0
print(arr_slice2) #[0,0]

print(arr_copy)



