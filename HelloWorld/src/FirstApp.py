'''
Created on Jul 22, 2015

@author: sen
'''

## ?
class Person:
    
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

## ?


hairs = ['brown', 'blond', 'red']
dictionary = {"val1": 1, "val2": 2}

def myFunction():
    print ("this")
                
def mySecondFunction(number):
    print ("this is the second function with an argument of "+ str(number))
    
def addFunction(num1, num2):
    return num1 + num2

def createFile():
    file_object = open("text.txt", "a")
    file_object.write("Hello File\n")
    file_object.close()
    
def ifStatement(num1, num2):
    if num1 > num2:
        print("1st is greater")
    else:
        print("2nd is greater")
    
def forLoop():
    for hair in hairs:
        print (hair)
        
def whileLoop():
    count = 0
    while count < 5:
        count = count+1
        print (count)
    
def addList():
    hairs.append("blue")
    print (len(hairs))
    print (hairs)
    
# A comment
print("Hello World")
print("Did you hear me?")
print("I said \"Hello World")

print ((2 + 2)% 4)

cars = 100

print ("Im rich! I have " +str(cars)+ " cars!")

myFunction()
mySecondFunction(2)

print (addFunction(2,2))

createFile()

ifStatement(3,6)

forLoop()

whileLoop()

addList()

print (dictionary['val1'])

me = Person("Sean", 23)

print (me.getName())

print (me.getAge())
