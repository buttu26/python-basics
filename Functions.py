#Functions:
#A function is a block of code that performs specific task.
#It allows us to group instructions together and reuse them whenever we needed.
#Instead of writing the same code again again , we just define a function once and call it whenever required
#syntax:
# def function_name(parameters):
#     #function body code
#     return value #optional
# function_name()
#example:
def greet():
    print("Hello World1")
greet()

#calling a Function:
# Calling a function means telling python to run the code inside a function by using it's name followed by paranthese().
#If the function needs input (parameter), we provide values (argument) inside the paranthese()
#When we call a function ,python jumps to the function ,excutes it's code,and then comes back to continue the program.
def greet():     
    print("Hello World")
greet()         #calling a function

def greet(name,branch):       #function name
    print("Hello World1",name,branch)
greet("Bittu","CSE AIML") # CALLING A FUNCTION

def greet():    
    print("Hello World")
greet()
greet()
greet()
greet()

#Passing Parameters and Arguments:
#Parameters: A variable declared inside the function definition.
#It's acts like an empty contaier waiting to receive a value.
#Arguments: The actual value as we pass into the function when calling it.It fills the empty container (parameter).
#example:
def greet(name): #name= parameter
    print("Hello",name)
greet("Bittu")

# #same task without function.
# Name="Bittu" #here name is input variable (parameter),and "bittu"is value to the parameter(argument).
# print("Hello",Name)

# #Types of Functions Arguments:

# #1. Positional Arguments: 
# #when we pass Arguments in the same order as the function parameter,they are called Positional Arguments,
# #Here order(position) is very important

# def greet(name,roll_no):      #step2 : values stores
#     print("Hello",name,"Your roll_no is",roll_no)    #step3: excecutes the line
# greet("Bittu","6L0")          #step1 : function calling

# #2. Keyword Arguments:
# #when we pass values or arguments by writing the parameter(variable=value), they are called Keyword Arguments
# def greet(name,roll_no): 
#     print("Hello",name,"Your roll_no is",roll_no)
# greet(name="Bittu",roll_no="6L0")

#3. Default Arguments:
#When a parameter has default value(assinging the value in parameter) in the functin definition ,it becomes a default argument.
def greet(name="student"): 
     print("Hello",name)
greet()
greet("lucky")

#4.Variable-length Arguments:
#sometimes we dont know how many arguments will be passed to a function .
#python provides two special ways to handle this:
#A. *args:(variable length arguments):
#L=10,20,30,40,50
def sum1(*list1):
     sum2=0
     for i in range(len(list1)):
          sum2=sum2+list1[i]
     print(sum2)
     print(type(list1))
sum1(10,20,30,40,50)

#B. **kwargs:(keyword variable-length arguments)
#collect multiple key=value pair into a dictionary.
def details(**info):
     for key,value in info.items():
          print(key,"=",value)
details(name="Bittu",roll_no="l60",branch="csm")

def details(**info):
     for i,j in info.items():
          print(i,"=",j)
details(name="Bittu",roll_no="l60",branch="csm")

#scope of variable :
x=10 #global variable
def var1():
     y=5 #local variable
     print('inside var1 function',x,y)
var1()
def var2():
     print("inside var2 function",x)
var2()

print("outside function",x)

