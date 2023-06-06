# now we will create an array. for that we have to import array
# While creating an array we have to specify codes
"""
Type Code   C Type                   Python type         size
b           signed char                int                  1
B           unsigned char               int                 1
u           Py_UNICODE              unicode character       2
h           signed short                int                 2
H           unsigned short              int                 2
i           signed int                  int                 2    You can assign -ive values
I           unsigned Int                int                 2    You cannot specify -ive values
l           signed Long                 int                 4
L           unsigned long               int                 4
f           float                       float               4
d           double                      double              8
"""
import array
from array import *


if __name__=="__main__":

    vals=array('i',[5,-6,3,7,3])
    print(vals.buffer_info)

    for i in range(len(vals)):
        print(vals[i],end=" ")
    print()

    # we can also iterate as:
    for i in vals:
        print(i,end=' ')
    print()

    #now lets suppose we want to copy array vals to newvals and we want to put squares to each number present in vals
    #vals.typecode means we want same typecode as like vals
    newvals=array(vals.typecode,(a*a for a in vals))
    print(newvals)

    print("Creating a dynamic array")
    arr=array('i',[])
    n=int(input("Enter length of array: "))
    for i in range(n):
        x=int(input("Enter value: "))
        arr.append(x)

    for i in arr:
        print(i,end=" ")
    print()
    print("Finding the index of a value: ")
    print(arr.index(12))








