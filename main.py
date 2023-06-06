# This is a sample Python script.
from unicodedata import decimal


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import math
def bitwiseOperators():
    # complement operator
    print("Bitwise operator")
    print(~12)
    #ouput will be -13 because firstly we take ones complement so it will be stored as 11110011 because binary of 12 is
    # 00001100 and taking its ones complement will give us 11110011 . When we print it ,so since 1 is there on first place
    # print function will take 2's complement and provide output with -ive sign
    print(12&13)
    print(12|13)
    #xor operator
    print(12^13)
    #left shift, shifting digits on left side , eg: binary value of 10 is 1010 , we can also write it as 1010.000, so shifting
    # 2 digits on left means 101000.0 which is the binary value of 40
    print(10<<2)
    #right shift
    print(10>>2)
def swapTwoNumbers():
    # in python we can simply swap two variables by writing
    print("Swap two numbers examples")
    a=10
    b=20
    a,b=b,a
    print(a,b)

def numberSystemConversionExamples():
    print("Number System Conversion Examples")
    #decimal to binary
    x=bin(25)
    print(x) # output will be 0b11001
    # binary to decimal
    bx=0b11001 # output will be 5
    # it will automatically get printed in decimal
    print(bx)
    y=oct(25)
    print(y)
    oy=0o31
    print(oy)
    z=hex(25)
    print(z)
    hexa= 0x10
    print(hexa)


def logicalOperatorExamples():
    print("LogicalOperatorsExamples")
    # we have not,'and' and or
    # to create boolean variable we can either assign True or False
    x,y=True,False
    print(x,y)






def dataTypesExamples():
    print("data types examples")
    b=5
    print(float(b))
    k=3
    c=complex(b,k)
    print(c)
    # list(range(10)) it will create a list from 0 to 9
    print(list(range(10)))
    print(list(range(2,10,2)))


def dictionaryExamples():
    map={1:"Khushi",2:"Raj",3:"Aarti"}
    print("Map examples")
    # identifying on the basis of keys
    print(map[1])
    # print(map[4]) if you tried to access a key that does not exists ,then it will throw error
    # to avoid termination,you can tell what to print if key does not exists
    print(map.get(4,"Not found"))
    # if we have two different list and we have to merge them into one:
    keys=[1,3,5,7]
    values=["Khushi","Stuti","Tashu","Siddhi"]
    k=dict(zip(keys,values));
    print(k)
    k[8]="Larry"
    print(k)
    # to delete
    del k[8]
    print(k)
    #map containing different values
    g={'Juhu':'Mumbai','Gateway of India':'Mumbai','Ujjain':['Mahakaleshwar','Sandipani','Mahakal Lok'],'Countries':{'America':1,'France':2,'UK':3,'Switzerland':4,'Singapore':5}}
    print(g)
    print(g['Countries'])
    print(g.keys())


def setExamples():
    print("Set examples")
    # set are used for storing unique elements
    # set does not maintain the insertion order
    # for set and map we use {}
    # in python , set does not sort the elements
    s={22,25,14,25,5}
    print(s)
    # to check the address of any variable ,write: id(a)
    # to know the type of any value write: type()
    


def tupleExamples():

    # unlike list, tuple is immutable,means you cannot change its value
    # to declare a tuple we have to use () rather than []
    print("Tuple Examples")
    tup=(12,44,100,98,23,56)
    print(tup[1])
    # you cannot change the value of any element




def listExamples():

        #   to create a list of list
        name = ["Khushi", "Kajal", "Aarti"]
        print(name)
        values = [100, 93, 98]
        print(values)
        merged = [name, values]
        print(merged)
        # to append in list
        name.append("Rashi")
        print(name)
        # insert
        name.insert(2, "Mansi")
        print(name)
        # remove  a particular element by passing the element name
        name.remove("Mansi")

        print(name)

        # you can also remove by passing index
        name.pop(1)
        print(name)
        # to directly remove the last one
        name.pop()
        print(name)
        # to delete multiple values
        del name[1:]
        print(name)
        # to add mutiple values,first put them in list and then extend
        name.extend(["Aarti","Kajal","Rashi","Mansi"])
        print(name)
        # other functions available are min,max,sum,sort


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # Some basic but important arithmetic operations
    a=5/2 # for float type value
    print(a)
    # for getting integer type value
    b=5//2
    print(b)

    # now lets suppose we want to find 2 to the power 3
    print(2**3)
    # to ignore the special behaviour of single or double quotes, we will give \
    # to print a string 3 times:
    print(3* "Khushi")

    print("c:\docs\nbcd")
    # but we will see that output is :     c:\docs
    #                                       bcd
    # It is because of the special character \n.So we wil python to treat that string as a raw string
    print(r'c:\docs\ncd')



# Press the green button in the gutter to run the script.
def mathFunctions():
    # for using math function we have to import math
    print("Math functions")
    print(math.sqrt(4))
    # floor
    print(math.floor(2.9)) # output will be 2 only
    #ceil
    print(math.ceil(2.2)) # output will be 3
    # if you don't want to write math again and again , we can write import math as m, so wherever we are writing math, we can
    # write m, m is an alias of math
    # power can be calculated via 2 methods :
    # priting 3 to the power 2
    print(3**2)
    # or by using pow function
    print(math.pow(3,2))
    # if you want to import specific function then you can write : from math import sqrt,pow




if __name__ == '__main__':
    print_hi('PyCharm')
    listExamples()
    tupleExamples()
    setExamples()
    dictionaryExamples()
    dataTypesExamples()
    logicalOperatorExamples()
    numberSystemConversionExamples()
    swapTwoNumbers()
    bitwiseOperators()
    mathFunctions()






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
