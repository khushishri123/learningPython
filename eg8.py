
from numpy import *
if __name__=="__main__":
     print("multidimensional array")
     # array package does not support mul. array ,for that we have to import numpy package
     # if you don't have numpy , in the console we have to write "pip3 install numpy"
     # in numpy while creating array we don't need to specify the type
     mularr = array([1, 3, 4])
     print(mularr.dtype) ## right now type will be int64
     # but if change any of its value to float ,then all the elements will become float type
     #using linspace , here too we have to specify start,end and paths in which we have to divide it
     # In linspace ,10 will be included
     a1=linspace(0,10,20)
     print(a1) # its type will be float
     # here we have arange, 20 is excluded
     a2=arange(1,20,2)
     print(a2)
     # we can also see the use logspace,zeros and ones
     # copying an array
     a3=array([1,4,9,16,25])
     a4=a3
     print(a4)
     # we can also add 2 array and assign it to some another one
     a5=a3+a4
     print(a5)
     # we can also print the sqrt of all the elements
     print(sqrt(a3))
     # we also max,min,log

     # now we have 2 options availble : shallow and deep copy
     # view is used for shallow copy , in shallow copy if you will change any element of one array ,it will automatically gets
     # changed in second array.But we don't want this to happen
     a6=a5.view()
     print(a6)
     a5[2]=20
     print(a6) # a6[2] will automatically got changed
     # for deep copy we will be using copy()
     a7=copy(a5)
     print(a7)
     a5[3]=40
     print(a7) # a7[3] will not get changed because we have performed deep copy
     #id will be different for all 3
     print(id(a5))
     print(id(a6))
     print(id(a7))
     # taking multidim. array
     a8=array([
          [1,2,3,4,5,6],
          [7,8,9,10,11,12]
     ])
     # converting 2d array into 1d
     a9=a8.flatten()
     print(a9)
     # 3 rows and 2 columns
     a10=a8.reshape(3,4)
     # we can also tell how many 2d array we want by passing 3 parameters to the reshape function
     # (2,2,3), so we want to create 2 2d array, having 2 rows and 3 columns
     print(a10)
     








