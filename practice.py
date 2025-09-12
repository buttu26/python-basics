#area of circle  
a=3.14
r=5
print(3.14*r*r)
print(3.14*r**2)

r=int(input("enter r value"))
print(3.14*r*r)


#area of triangle
height=5
base=3
print(0.5*height*base)
print(1/2 * base*height)

height=int(input("enter a value: "))
base=int(input("enter base:"))
aot=1/2 * base * height
print(aot)

#squares and cubes of a number
a=int(input("enter a value :"))
square= a ** 2
cube=a**3
print(square)
print(cube)
b=int(input("enter b value: "))
square1=b**2
cube1=b**3
print(square1)
print(cube1)

#KM-> METER   METER-> CENTIMETER

distance=25 #km
kilometer=distance/1000
meter=distance*1000
m1=distance/1000
centimeter=distance*100
miles=distance*1.6
print(kilometer)

distance = 50 #meters    #1meter=100cm
centimeter=distance/100
print(distance)


#find the number is even or odd
number=int(input("enter value: "))
if(number%2 == 0):
    print(" number is even")

else:
    print("number is odd")


#to find the candidate has an voter id

age= int(input("enter age:"))
if(age>=18):
    if(age>=100):
        print("he/she has a voter id but he/she might be dead")
    else:
        print("they can vote")    
else:
    print("underage not valid")

#checking a year is a leap year or not

year=int(input("enter no,of year"))
if(year%4==0 and year%100!=0) or year%400==0:
    print("its a leap year")
else:
    print("its not a leap year")

#practice questions
# write a program to find the average of all numbers in a list
 
list1=[1,2,3,4,5]
l=len(list1)
sum=sum(list1)
print(sum/l)


# count how many positive negative and zero values are in a list

list2=[-2,-3,6,5,-8,4,0,10,0]
list1=[]
list3=[]
list4=[]

for num in list2:
   if (num>0):
     list1.append(num)
print(list1)
for num in list2:
   if (num<0):
      list3.append(num)
for num in list2:
   if (num==0):
     list4.append(num)
print(list3)
positive_num=len(list1)
negative_num=len(list3)
zeroes_=len(list4)
print(positive_num)
print(negative_num)
print(zeroes_)

# remove duplicate elements from a list

list1=[-2,-3,6,5,-8,4,0,10,0]
list1.pop(-1)
print(list1)


# write a program to seperate even and odd numbers into two new lists

list1=[1,2,3,4,5,6]
list2=[]
list3=[]
for num in list1:
   if (num%2==0):
      list2.append(num)
print(list2)
for num in list1:
   if (num%2!=0):
      list3.append(num)
print(list3)


# take a list of names and print the longest name

list1=["laxmi narasimha reddy","sadvik yadav","charan teja","sreekar reddy"] 
list1.sort()
print(list1)
print(list1[1])
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
