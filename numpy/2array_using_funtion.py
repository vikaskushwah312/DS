#crete array using numpy funtions
#zeros,
#ones,
#eye
#diag
#randint
#rand
#randn
import numpy as np

# arr=np.zeros((2,3))
# arr=np.ones((3,2))
arr_eye=np.eye(3)
#diegonal one rahega baki sab zeros hoge

#parameter take one list
# arr=np.diag([1,2,3])
#diagonal is 1,2,3 and rest of number is zeros

#find the diagonal of any materix
# print(np.diag(arr_eye))

"""For geting the random number  
randint(inclusive,excluxive,kitani values chahiye)
"""
# arr=np.random.randint(1,15,4)

arr=np.random.rand(4)
arr_2d=np.random.rand(2,3)

''' This is working on standrd normal distributaion'''
arr=np.random.randn(4)
print(arr)

