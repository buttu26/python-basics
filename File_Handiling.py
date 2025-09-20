# # file=open("students.txt","w")
# # print("file created")
# # file.close

# #syntax of file handiling:
# #Reading:
# file=open("students.txt","r")         # mode = r, w, a, rb, wb, r+, w+
# print(file.read())
# file.close()

# file=open("students.txt","r")  
# content=(file.read())     
# print(content)
# file.close()

# #Types of Read:
# #1.read(): 
# file=open("students.txt","r")     
# print(file.read())
# file.close()

# #2.readline():
# file=open("students.txt","r")  
# content=(file.readline()) #1st line
# content1=(file.readline())   #2nd line    
# print(content)
# print(content1)
# file.close()

# #3.readlines():
# file=open("students.txt","r")
# content=(file.readlines())
# print(content)
# file.close()

# # Write():

# file=open("students.txt","w")
# print("file created")
# file.close

# file=open("students.txt","w")
# file.write("hello bittu \n")
# file.write("hello lucky \n")
# file.close()
# print("Data written sucessfully")

# #writing multiple lines at once
# lines = ["Nandan\n", "Aarav\n", "Priya\n"]
# file = open("students.txt", "w")
# file.writelines(lines)
# file.close()

# #append():
# file=open("students.txt","a")
# file.write("hello bittu \n")
# file.close()
# print("Data written sucessfully")

# #read
# file = open("students.txt", "r") # open in read mode
# content = file.read() # read whole file
# print("File Content:\n", content)
# file.close()

