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
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         