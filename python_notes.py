#python notes

print ("hello world") 
#prints hello world

carname = "Volvo"
#variable assigns value to volvo
x = 50
#variable x is = 50

x = 5
y = 10 
print(x + y)
#prints x+y (5+10)

x = 5
y = 10
z = x + y
print(z)
#prints what z is

len() #returns number of items in a object or table

#e.g 
mylist = ["apple", "banana", "cherry"]
x = len(mylist) #print 3

#Python numbers
x = 1 # int whole number only positive or negative e.g -290 = integer (int)
y = 2.8 # float float is a number positive or negative containing one or more decimals (can also be scientific number with e which would be to the power of th 10)
z = 1j # complex  complex numbers just written with a j as the imaginary part

#Strings
x = str("s6") #will be 's6'
y = str(3) #will be '3'
z = str(3.0) #will be '3.0'

#Boolean = true and false

#input
username = input("Enter username:")
print("Username is: " + username)

# Data Types
# Text Type str
# Numeric Types int, float, complex
# Sequence Types list tuple, range
# Mapping Type dict
# Set Types set, frozenset
#tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets. thistuple = ("apple", "banana", "cherry")
x = frozenset({"apple", "banana", "cherry"}) #unchangeable objects

#indexing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #prints 3-5
#negative indexing
-1 #refers to last
-2 #refers to second last etc.
print(thistuple[-4:-1])

#HOW TO ADD TUPLE WITH 1 ITEM
thistuple = ("apple",) #remember comma!
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

0 #is the first item in the object

#len
print(len(thistuple)) #will return the length of the char for this ex down it will print 7

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

#del
x = "hello"

del x #used to delete variables, lists, or parts of a list etc. In this example it will error because x variable is no longer defined

print(x)

append() # method appends(adds aka) an element to the end of the list.

#eg.
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

#appending lists into other lists
print(fruits) #oranges will added to the end of the list next to cherry

a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

a.append(b) #you append lists within lists

print(a)

#add()
#The add() method adds an element to the set.

fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)

#upper
txt = "Hello my friends"

x = txt.upper() #makes it upper case

print(x)

#same thing goes for lower 


#strip
txt =" banana "  

txt.strip()

"""removes any white space
"""
print(txt)

#replace()

string.replace(oldvalue, newvalue, count)

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

#######################################################
txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)

#insert()

#The insert() method only inserts the element to the list. It doesn't return anything; returns

# vowel list
vowel = ['a', 'e', 'i', 'u']

# inserting element to list at 4th position
vowel.insert(3, 'o')

print('Updated List: ', vowel)


#get()

""""
multi line note
""""
dictionary.get(keyname, value)

car = { --dictionary
  "brand": "Ford",
  "model": "Mustang",
  --keyname"year": 1964 -- value
}

x = car.get("model")

print(x)


#display the data type of x:
print(type(x)) 

# Boolean Type bool
#binary Types: bytes, bytearray, memoryview


#Integer
#Float
#Characters 1 character assgined to a variable ex. x = "c"
#Strings

print(type(z)) #will print the type of data

print(int(2.4)) # print integer version of 2.4 which would be 2, this can be done for other data types such as boolean
print(bool(2.4))
print(bool(2.4))
print(float(3))
print(str(2.4))


# >= greater than and equal to <= lower than and equal to, == to check if two values are equal != not equal to
# and or are used for complex conditions

# ":" is equal to then so basically : means then

x = 5
y = 6

if y> x:
  print("Y is greater than X")
elif x> x:
  print("Y is not greater than X")

#while loops

x = 20

while x> 0:
    print(x)
    x = x-2

#for loops
x = 10

for i in range(x): #prints x 10 times
    print(x)

for i in range(x, 10): #prints 10 10 times
    print(x)

for i in range(0, x, 2): # how it long it takes for *2 to reach 10 which would be 5 because 5*2 = 10
    print(x)

    for i in range(x, 0, -1): #prints 20 times the third area it how it will be counted
        print(x)


 #Kaggle       
 #yorkcshub@gmail.com

#Operators 
#addition = + 
# subtraction = -
#multiplication = *
#exponentiation = **
#division = /
#integer divsion = //
#modulo remainder = %


#A value has a memory address.
#A variable contains a memory address.
#A variable refers to a value.
#A variable points to a value.
#Example: Value 8.5 has memory address id34.
#Variable shoe_size contains memory address id34.
#The value of shoe_size is 8.5.
#shoe_size refers to value 8.5.
#shoe_size points to value 8.5.