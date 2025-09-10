# # collection datatypes
# #example
# list1=[10,20,30,40,50]
# fruits=["apple","banana","watermelon"]
# list2=[10.1,20.2,30.3,40.4,50.5]
# list3=[True,False,True,False]
# list4=[10,20.2,"hello",True,"False"]
# print(list1)
# print(fruits)
# print(list2)
# print(list3)
# print(list4)

# list1=[10,20,30,40,50]
# print(list1[-1])
# print(list1[-2])
# print(list1[-3])
# print(list1[-4])

# list1=[10,20,30,40,50]
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[4])

# #slicing
# list1=[10,20,30,40,50]
# print(list1[2:4])

# slc1=["prabhas","mahesh babu","allu arjun","jmr","mallareddy"]
# print(slc1[0:5])
# print(slc1[0:4])
# print(slc1[-3])

# # adding elements in list:
# # append
# kalkicast=["prabhas","kamalhasan","amithabhachan","dipika padukon","ssr"]
# print(kalkicast)
# kalkicast.append("deesha patani")
# print(kalkicast)

# #insert:
# kalkicast=["prabhas","kamalhasan","amithabhachan","dipika padukon","ssr"]
# kalkicast.insert(4,"vijay devarakonda")
# print(kalkicast)

# #extending:

# kalkicast=["prabhas","kamalhasan","amithabhachan","dipika padukon","ssr"]
# kalkicast.extend(["anudeep","mrunal thakur"])
# print(kalkicast)             

# #removing element in list:
# #1.remove():
# kalkicast.remove("dipika padukon")
# print(kalkicast)

# #2.pop():
# kalkicast.pop(4)
# print(kalkicast)

# #3.clear():
# kalkicast.clear()
# print(kalkicast)

# #changing the elements:
# kalkicast=["prabhas","kamalhasan","amithabhachan","dipika padukon","ssr"]
# kalkicast[1]="sandeep reddy vanga"
# print(kalkicast)

# #mathematical operations:
# #1.concatation:
# a=[1,2]
# b=[3,4]
# c=a+b
# print(c)

# #repeation:
# a=[1,2]
# n=int(input("enter the n value:"))
# b=a*n
# print(b)

# #searching and checking
# #in
# a=[2,4,6,8,10,12,14]
# if 2 in a:
#     print("yes item is pressent in the list")

# #not in
# a=[2,4,6,8,10,12,14]
# if 3 not in a:
#     print("3 is not in a")

# #index():
# a=[2,4,6,8,10,12,14]
# print(a.index(8))     #3

# #count():    which gives the no.of times a particular item is repeated
# a=[2,4,6,8,8,10,12,14]
# print(a.count(8))     #2
# print(a.count(2))     #1

# a=[2,4,6,8,8,8,10,12,14]
# cnt=0
# print(a.count(8))
# for i in range(10):
#     a.append(i)
#     if i == 8:
#         cnt=cnt+1
# print(cnt)

# #sorting: sort()
# st=[25,12,5,31,18,13,7,45,8,55,68]
# # ascending order {5,7,8,12,13,18,25,31,45,55,68}
# st.sort()
# print(st)
# #descending order {68,55,45,31,25,18,13,12,8,7,5}
# st.reverse()
# print(st)

# st1=[25,8,4,7,10] #d.o {25,10,8,7,4}
# st1.sort(reverse=True)
# print(st1)

# #copying the list
# frd1=["A","C","D","A","D","B","B","C","C","A","A"]
# frd2=frd1.copy()
# print(frd2)


# frd1=["A","C","D","A","D","B","B","C","C","A","A"]
# frd2=frd1.copy()
# frd2[2]="B"
# print(frd2)

# #Built-in Functions with loops

# st=[25,12,5,31,18,13,7,45,8,55,68]

# #len(): Return the number of elements
# print(len(st))                                              #11
# #max(): Returns the maximum elements in the list
# print(max(st))                                              #68
# #min(): Returns the minimum elements in the list
# print(min(st))                                              #5
# #sum(): Returns the total sum of all the list elements
# print(sum(st))                                             #287

# #sort vadina vadakapoina same answers vasthayi

# st=[25,12,5,31,18,13,7,45,8,55,68]
# st.sort()
# #len(): Return the number of elements
# print(len(st))                                              #11
# #max(): Returns the maximum elements in the list
# print(max(st))                                              #68
# #min(): Returns the minimum elements in the list
# print(min(st))                                              #5
# #sum(): Returns the total sum of all the list elements
# print(sum(st))                                             #287

# #spliting   to split the given data 
# a="hello world to the python programming"
# b=a.split()
# print(b)

# #multiple values using input data to the list : 

# a=input("enter multiple values:").split()      # ['10','20','30','40','50']  #output is string
# print(a)                                       
# #list=[10,20,30,40,50]      integers

# #multiple values using input data to the list : map()
# a=map(int,input("enter multiple values: ").split())
# print(a)

# a=list(map(int,input("enter multiple values: ").split()))
# a.sort()
# print(a)       #[10,20,30,40,50] #integer values

# b=input("enter the multiple values:").split()           # 10 20 30 40 50
# print(b)  #['10','20','30','40','50']       #string values

#traversing a list
# cars=["alto","thar","bmw","porsche","rolls royce"]
# for car in cars:
#     print("cars=",car)

# #using index with loops
# a=len(cars)      #4
# for i in range(0,5):
#     print("cars",i,cars[i])

# # Adding elements using for loop

# list1=[]
# n=int(input("enter the number of list values"))
# for i in range(0,n):
#     a=input("enter the list values : ")
#     list1.append(a)
# print(list1)

# # give the input values to the lists from 0 to 10
# list1=[]
# n=int(input("enter the number of list values"))
# for i in range(0,n):
#     list1.append(i)
# print(list1)

#sum of list items = 10 20 30 40 50 without using sum()

# list1=[10,20,30,40,50]
# sum=0
# for i in list1:
#     sum= sum + i
# print(sum)

# #multiply
# list1=[10,20,30,40,50]
# product=1
# for i in list1:
#     product= product * i
# print(product)

# #convert ["p","y","t","h","o","n"] to python

# list=["p","y","t","h","o","n"]
# result="".join(list)
# print(result)

# #or
# list1=["p","y","t","h","o","n"]
# word=""
# for i in list1:
#     word=word+i
# print(word)

#find the maximum amd minimum number from list without using max()
list1=[17,7,100,102,229,103,227,277]
list1.sort()
print(list1)

list1=[17,7,100,102,229,103,227,277]
list1.sort()
print(list1)
print("max value of list:",list1[7])
print("min value of the list:",list1[0])


#find the maximum and minimum numbers of the list without using max() and min() and sort().
list1=[17,7,100,102,229,103,227,277]
max1=list1[0]
min1=list1[0]
for num in list1:
    if num>max1:
        max1=num
    if num < min1:
        min1=num
print(max1)
print(min1)
    