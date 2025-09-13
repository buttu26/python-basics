# #sets:
# #syntax:     { }
# #My_set= {element1,element2,element3}

# #characteristics of sets
# #unordered:
# #example  {1,2,3}  and {3,2,1} are considered the same set.
# #unindexed: you cannot access set elements by the index like lists or tuples.

# #a={1,1,2,3,4} 
# #print(a[1])                          #TypeError: 'set' object is not subscriptable

# #unique values only: duplicate values will be automatically removed from the list
# a={1,1,1,2,2,3,4,4,4}
# print(a)                                    #output  {1,2,3,4}

# #creating a set:
# s1={1,2.3}
# s2={10,12.5,"hello",True}
# s31={}          #empty dictonary
# s3=set()        #empty set
# print(type(s3))
# print(type(s31))

# #accessing sets :  we cannot access a element using a element but we can access an element using loops. 

# s1={"Rajinikanth","Snake king","Monica"}
# for role in s1:
#     print(role)

# #ADDING AN ELEMENT IN SET
# A={1,2,3,4}
# A.add(5)               #adds only single element in any elements
# A.update([26,13])      #adds the multiple values in the set
# print(A)             
# #DELETING THE ELEMENTS IN SET:
# #1.remove():
# A.remove(2)                 #{1,2,3,4,5,13,26}
# print(A)                  #OUTPUT {1,3,4,5,13,26}
# #2.discard();      removes the element but it gives no error if the value is not found in the set
# A.discard(3)              #output {1,4,5,13,26}
# print(A)
# #3.pop():    remove the random element from the set.
# A={12,18,20,25,34,29,25}
# A.pop()
# print(A)
# #4.clear():   removes all the elements from the set
# A={12,18,20,25,34,29,25}
# A.clear()
# print(A)

#mathemetical operations in set:
#1.Union: "|"          prints all unique values or elements from the both sides
A={1,2,3,4}
B={3,4,5,6}
print(A|B)            #output {1,2,3,4,5,6}
#2.intersection  "&" 
A={1,2,3,4}
B={3,4,5,6}
print(A&B)    
#3.difference: "-"      REMOVES THE COMMON ELEMENTS FROM THE LIST BUT PRINTS ONLY THE FIRST SETS VALUES ONLY.
A={1,2,3,4}
B={3,4,5,6}
print(A-B)           #OUTPUT {1,2}
print(B-A)           #OUTPUT {5,6}
#4.Symmetric difference:     "^"
   #REMOVES THE COMMON ELEMENTS FROM THE LISTS BUT PRINTS BOTH SETS VALUES.
A={1,2,3,4}
B={3,4,5,6} 
print(A ^ B)

#Mathemetical operations using functions:
#1.Union
print(A.union(B))                          #{1,2,3,4,5,6}
#2.intersection
print(A.intersection(B))                   #{3,4}
#3.Difference
print(A.difference(B))                     #{1,2}
#4.Symmetric difference
print(A.symmetric_difference(B))           #{1,2,5,6}