# #Dictionary:
# #syntax : {}


# # l=[10,20,30,40]
# # t={10,20(30,40),50}         #nested tuple

# My_Dictionary={                #keys can be
#      1:"value1",               # integer
#     10.2:"value2",             #float
#     "key3":"value3",           #string
#     "key4":"value4"            
# }
# print(My_Dictionary)

# #Characteristics of dictionary:
# #1.key-value pairs:every entry of dictionary's element is a pair: keys and values
#                                                              #     {"name":"bittu"}
# #2.unique keys
# A={"n":"Bittu","n":"anurag"}
# print(A)                              #"n":anurag
# #keys must be immutable:
# #keys can be (valid keys : integer , float, string)
# #example is 
# My_Dictionary={                
#      1:"value1",              
#     10.2:"value2",            
#     "key3":"value3",         
#     "key4":"value4" 
# }
# print(My_Dictionary)

# #creating Dictionary:
# #1.Normal Dictionary:
# Biodata = {
#     "Name":"Bittu",
#     "Roll_no": "6L0",
#     "Branch":"CSE AIML",
#     "Place":"Balapur"
# }
# print(Biodata)
# #2.Dictionary using constructors:
# Biodata = dict(Name="Bittu",Roll_no="6L0", Branch="CSE AIML", Place="Balapur")
# print(Biodata)
# #3.Empty Dictionary
# E_D={}
# print(E_D)
# #4.Accessing the dictionary:
# #-> To access an element we use key names inside the square brackets[] or we can use get() method
# Biodata = {
#     "Name":"Bittu",
#     "Roll_no": "6L0",
#     "Branch":"CSE AIML",
#     "Place":"Balapur"
# }
# #using square brackets []
# print(Biodata["Name"])            #Bittu
# print(Biodata["Roll_no"])         #6L0
# print(Biodata["Branch"])          #CSE AIML
# print(Biodata["Place"])           #Balapur
# #print(Biodata["Age"])       #error vasthadhi bcz "Age" key create cheyaledhu kabatti

# #Using get() method
# print(Biodata.get("Name"))        #Bittu
# print(Biodata.get("Roll_no"))     #6L0
# print(Biodata.get("Branch"))      #CSE AIML
# print(Biodata.get("Place"))       #Balapur
# print(Biodata.get("Age"))         #None   vasthadhi even if there is no Age key

# #Adding and Updating Dictionary:
# #1.Adding:  You can insert a new key-value pair into a dictionary.
# Biodata = {
#     "Name":"Bittu",
#     "Roll_no": "6L0",
#     "Branch":"CSE AIML",
#     "Place":"Balapur"
# }
# Biodata["Age"]=18         #adding new key and value
# print(Biodata)

# #2.Updating:  You can update or change the values using existing dictionary
# Biodata["Place"]="Rangareddy"   #updating the existed value of a key
# print(Biodata)

# #Removing in the Dictionary:
# #python gives multiple ways to delete items from a dictionary.
# #1.pop()

# Biodata = {
#     "Name":"Bittu",
#     "Roll_no": "6L0",
#     "Branch":"CSE AIML",
#     "Place":"Balapur"
# }
# Biodata.pop("Name")            #removes the key  AND value
# print(Biodata)

# # 2.popitem()
# Biodata.popitem()            #removes the last inserted item from a dictionary
# print(Biodata)  
# # 3.clear()
# Biodata.clear()              #removes EVERY the elements in the dictionary
# print(Biodata)             
# # 4.delete
# Biodata = {
#     "Name":"Bittu",
#     "Roll_no": "6L0",
#     "Branch":"CSE AIML",
#     "Place":"Balapur"
# }
# del Biodata["Branch"]
# print(Biodata)            #DELETES THE KEY FROM THE DICTIONARY

# Biodata = {
#     "Name":"Bittu",
#     "Roll_no": "6L0",
#     "Branch":"CSE AIML",
#     "Place":"Balapur",
#     "Role":"Software developer"
# }
# #keys(): It prints only the keys of dictionary
# print(Biodata.keys())
# #values(): It prints only the values of dictionary
# print(Biodata.values())
# #items(): it prints onlt the keys and values of dictionary
# print(Biodata.items())

# #updating update():
# Biodata.update({"Role":"Web Developer","Place":"Hyderabad"})
# print(Biodata)

#loops for dictionary