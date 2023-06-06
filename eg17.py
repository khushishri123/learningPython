from functools import *
def is_even(n):
    return n%2==0

if __name__=="__main__":
    # here we will learn about map,reduce anf filter
    # filter will take a sequence and will return a sequence . So we want to filter out even numbers
    #filter takes 2 arguments in which first one if the function in which you mention the logic and second one is the sequence
    # on which you want to perform operations

    nums=[20,13,17,432,23,22,100]

    even=list(filter(is_even,nums))# filter return sequence but we want list, so for that we will convert it into list
    print("Even: ",even)

    # but we can directly pass a lambda expression to filter
    odd=list(filter(lambda a: a%2==1,nums))
    print("Odd: ",odd)

    # remember one thing that you cannot use filter to perform sum, multiplication or some other calculation. It is used only for
    # filtering out elements. Which satisfy the condition will be the part of sequence and it will discard the rest
    # for doubling all the elemnts we will be using map and when we want single output for all the list elements we will use reduce
    # filter: for fitering out list elements
    # map: for performing some operations on all the list elements
    # reduce: for getting a single output, for reduce we have to import functools
    doubles= list(map(lambda a: a*2, even))
    print("Doubling even numbers: ",doubles)
    # for getting sum for doubles, at one point reduce wil take 2 values
    sum=reduce(lambda a,b:a+b,doubles)
    print("Sum of doubles : ",sum)
    

