from numpy import *
if __name__=="__main__":
    # we will learn how to create a matrix
    #first we will create a matric with the help of array
    a1=array([[1,2,3],
             [4,5,6]])
    m=matrix(a1)
    print(m)
    # we can also create it independently
    m2=matrix('11 21 31 ; 41 51 61 ; 23 43 44')
    print(m2)
    # if you just want to print diagonal value of the matrix,
    print("Diagonal values: ")
    print(diagonal(m2))
    # to find the min and max we have m2.min() and m2.max()
    # Also to mutiply 2 matrices, for multiplications number of rows and columns should be same
    m3=matrix('1 2 3 ; 4 5 6 ; 33 34 22')
    m4 = m2 * m3
    print(m4)
    
