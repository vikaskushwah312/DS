import numpy as np
''' One-D Array '''

arr=np.array([10,20,30,40,50,60])

# print(arr[0]) #10
# print(arr[-1]) #60

# print(arr[0:3]) #10 20 30 


'''For Two-D Array '''

materix=np.array([[10,20,30],[40,50,60],[70,80,90]])

#Indexing using double braket notation

# print(materix[0][1]) #20
# print(materix[2][2]) #90

#Indexing using single Braket Notation

# print(materix[0,1]) #20
# print(materix[2,2]) #90

'''Sliceing for Two-D Array'''
# print(materix[:2]) #[[10,20,30],[40,50,60]]

# print(materix[:2,0:2]) #[[10,20],[40,50]]

# print(materix[1:,1:]) #[[50,60],[70,80]]

'''Example '''
np.random.seed(123)
materix2 = np.random.randint(1,101,25).reshape(5,5)
print(materix2)
print(materix2[1:4,1:4])






