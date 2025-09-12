# #Tuples

# #example
# coordinates=("x","y")
# my_tuple=(10,20,30)
# print(my_tuple)
# print(type(my_tuple))
# print(coordinates)

# #creating a Tuple:
# #empty tuple
# et=()
# print(et)
# #tuple with numbers:
# n=(1,2,3,4,5,6)

# #tuple with strings
# s=("a","b","c")
# #tuple with mixed datatypes
# m=(24,3.14,"A","C",True,"False")

# #tuple with single element
# a=10
# b=[10]
# c=(10)
# d=(10,)
# print(type(a))     #integer
# print(type(b))     #list
# print(type(c))     #integer
# print(type(d))     #tuple

# #accessing elements

# a=(10,20,30)
# #i  0  1  2     indexes
# #i -3 -2 -1     -ve indexes
# print(a[2])
# print(a[0])
# print(a[1])
# print(a[-2])
# print(a[-3])
# print(a[-1])

# #slicing the tuple
# #extracts the part of the tuple using starting index and end index
# #([start index:end index])
# #In tuple it will print before the end index value. 

# tuple=("apple","bot","cat",4)
# print(tuple[0:2])           #('apple', 'bot')
# print(tuple[0:1])           #('apple',)
# print(tuple[0:3])           #('apple', 'bot', 'cat')
# print(tuple[-4:-1])         #('apple', 'bot', 'cat')
# print(tuple[-3:-1])         #('bot', 'cat')
# print(tuple[-2:-1])         #('cat',)

# # changing the values
# # tuples are immutable so we cannot change the values.
# # A=(10,20,30,)
# # A[1]=50            #TypeError'tuple' object does not support item assignment
# # print(A)

# # Append
# # A=(10,20,30,40)
# # A.append(50)
# # print(A)            # AttributeError: 'tuple' object has no attribute 'append'

# #length
# A=(10,20,30,40)
# print(len(A))

# #max:
# A=(10,20,30,40)
# print(max(A))

# #min
# A=(10,20,30,40)
# print(min(A))

# #sum
# A=(10,20,30,40)
# print(sum(A))

# #concatenation
# A=(10,20,30,40)
# B=(50,60,70)
# C=A+B
# print(C)

# #repetition
# A=(10,20,30,40)
# n=int(input("enter the n value:"))
# b=A*n
# print(b)

# #SEARCHING AND CHECKING
# A=(10,20,30,40)
# if 20 in A:
#     print("yes its there")

# #not in
# if 50 not in A:
#     print("no in A")

# #Index():
# A=(10,20,30,40)
# print(A.index(20))

# #count():
# A=(10,20,30,40,40)
# print(A.count(40))

# #sorting  reversing is not valid for tuples

# # A=(10,20,30,40,40,5)
# # A.sort()
# # print(A)         #AttributeError: 'tuple' object has no attribute 'sort'

# #COPYING THE TUPLES
# # A=(10,20,30,40)
# # B=A.copy()
# # print(B)

#Iterating tuple using for loop

