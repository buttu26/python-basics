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

