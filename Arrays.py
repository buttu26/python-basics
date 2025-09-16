#Arrays in python:
L=[10,10.5,"Hello",True]             #list has all mixed datatypes
A=[10,20,30,40,50]                   #no mixed datatypes in arrays
A=[10.5,20.5,30.5,40.5,50.5]

#Array vs Lists
#importing the array module.
import array as arr

#creating an aray:
Numbers=arr.array('i',[1,2,3,4,5])            #'i' = integer      'u' = string     'f'= float
                  #i   0 1 2 3 4
print(type(Numbers))
print(Numbers)

#Accessing Array Elements
print(Numbers[3])     #4
print(Numbers[-1])    #5               

#Adding An Element in Arrays:
#1.Append():
Numbers.append(7)
print(Numbers)
#2.insert()
Numbers.insert(5,6)
print(Numbers)
#3.extend()
Numbers.extend([8,9,10])
print(Numbers)

#Removing an element in Arrays:
#1.remove()
Numbers.remove(2)
print(Numbers)
#2.pop()
Numbers.pop(-1)
print(Numbers)
#3.clear()
Numbers.clear()
print(Numbers)

#Changing the elements
Numbers=[1,2,3,4,5]
Numbers[1]=10
print(Numbers)

#looping arrays
for i in Numbers:
    print(i)

#Basic Operations on Arrays:
#1.len()
print(len(Numbers))
#2.max():
print(max(Numbers))
#3.min():
print(min(Numbers))
#4.sum()
print(sum(Numbers))