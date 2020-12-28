import numpy as np

arr= np.random.randint(1,100,20)
reshape_arr = arr.reshape(2,10)

'''Convert again 2D to D '''
one_d= reshape_arr.reshape(20)

# print(one_d)

arr2= np.random.randint(1,100,50)
# print(arr2)

'''for 3d '''
three_d = arr2.reshape(2,5,5)
# print(three_d)

'''Convert again 3D to D '''
arr2= three_d.reshape(50)
# print(arr2)

'''For -index'''
arr=np.arange(20)
print(arr.reshape(-1,4))
print(arr.reshape(5,-1))
