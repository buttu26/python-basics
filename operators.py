# arthemetic operator
a=10
b=3
print(a+b) 
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

# comparision operator
x=5
y=8
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#logical operators
#AND OPERATOR
x=5
y=10
print(x>4 and y<15)
print(x>3 and y<5)
print(x<2 and y<10)
print(x>10 and y<5)
#OR OPERATOR
x=55
y=10
print(x<60 or y>7)
print(x<56 or y<5)
print(x<50 or y>8)
print(x<55 or y>11)
#NOT OPERATORS
p=5
q=0
print(not(p))
print(not(q))
x=5
y=10
print(not(x>4 and y<15))
print(not(x>3 and y<5))
print(not(x<2 and y<10))
print(not(x>10 and y<5))

#ASSIGNEMENT OPERATORS

x=15
x=x+5
print(x)
x=15
x+=5
print(x)
x=50
x-=3
print(x)
x=45
x*=2
print(x)
x=35
x/=5
print(x)
x=35
x//=5
print(x)
x=50
x%=5
print(x)
x=2
x**=5
print(x)

#bitwise operators

x=5
y=3
print(x & y)      #and shift
print(x|y)        #or shift
print(~x)         #not shift
print(x^y)        #xor shift
print(x<<y)       #right shift
print(x>>y)       #left shift

a=5
b=10
print(a&b)      #output 0    refer notes for clarity
print(a|b)      #output 15   refer notes for clarity
print(~a)
print(a^b)
print(a<<b)     #output example in notes left shift
print(a>>b)     #output example in notes right shift

#IDENTY OPERATOR
x=[1,2,3,4]
y=x
z=[1,2,3,4]

print(x is  y)        # true 
print(y is not z)     #true
print(x is z)         #false
print(x is not z)     #true

#MEMBERSHIP OPERATORS
text = "sairam"
print("sai" in text)        #true
print("b" in text)          #false
text=[1,2,3,4]
print(4 in text)            #true
print(4 not in text)        #false

