#Numpy:
#Numpy (Numerical Python) is a python library used for scientific and mathematical computing.
# It provides:
# -> Powerful array objects for our python program(more effective than python lists.)
# -> Vectorized operations (Fast element wise calculations.)
# -> Supports for linear algebra , statistics , Random numbers operations etc..

#importing the numpy library.
import numpy as np
aa=np.array([1,2,3])
print(aa)

import array as arr
#creating an array with numpy:
#1-D array
A1D=np.array([1,2,3,4,5,6,7])
print(A1D)
#2-D array
A2D=np.array([[1,2,3],[4,5,6],[7,8,9]])
# [ 
#     1 2 3
#     4 5 6
#     7 8 9
# ]
print(A2D)

#METHODS AND OPERATIONS IN NUMPY ARRAY
#1.Basic Array Information methods:
A=np.array([1,2,3,4,5])
#ndim(): returns the  dimensions of the array
print(A.ndim)           #1
print(A2D.ndim)         #2
#shape: returns a tuple showing the sizes of the array in each dimensions(rows,columns,etc..)
print(A2D.shape)           #(3,3)  (rows,columns)
#size: it returns the total no.of elements in the array.
print(A2D.size)        #9
#dtype: returns the datatypes of the elements in the array.
print(A2D.dtype)           #type = int64

#2.Creating an array with numpy:
#zeroes:
print(np.zeros(7))

#ones:
print(np.ones(7))

#arange:
print(np.arange(1,11,1))
print(np.arange(0,11,2))
print(np.arange(1,11,2))

#linspace: it creates 3 numbers evenly spaced between 0 and 1  
print(np.linspace(0,1,15))      # 0  0.5  1

#mathematical operations:
A=np.array([1,2,3,4,5])            #l=[1,2,3,4,5]   print(A+6)  is not valid bcz its int 
print(A+6)
print(A-2)
print(A*2)
print(A/2)
print(A//2)
print(A%2)
print(A**6)
AA=[]
for i in A:
    AA.append(i+6)
print(AA)

#Aggregste Functions:
A=np.array([1,2,3,4,5])
#sum():
print(np.sum(A))     #15
#mean():
print(np.mean(A))    #3
# max()
print(np.max(A))     #5
#min():
print(np.min(A))     #1
#median():
print(np.median(A))  #3
#std:
print(np.std(A))     #standard division = 1.4142135623730951
#cumprod:
print(np.cumprod(A))

#Matrix operations
mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])
#[
#    1 2 3
#    4 5 6
#    7 8 9
# ]
mat2=np.array([[9,8,7],[6,5,4],[3,2,1]])
#[
#     9 8 7
#     6 5 4 
#     3 2 1
# ]
print(mat1+mat2)
print(mat1**mat2)
print(mat1*mat2)
#dot():
print(np.dot(mat1,mat2))

#transpose():
print(np.transpose(mat1))
print(np.transpose(mat2))
