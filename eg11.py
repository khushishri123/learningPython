def update(x):
    print("Before updation: ",id(x)) # till now the id of a and x will be same , but as soon as we change the value x , new memory will be
    # allocated for x
    x=10
    print("After updateion: ",id(x))
    print("x: ",x)
    # we are updating the value of x but it will not affect the value of a
    # so in python there is no concept of pass by value or pass by reference


def updateList(l):
    print(id(l))
    l[1]=25
    print("l: ",l)


if __name__=="__main__":
    # now we will learn the concept pass by value and pass by reference
    a=8
    print(id(a))
    update(a)
    print("a: ",a)

    # if we try to update list then it can update original listr too.This is because list are mutable.Id will be same
    # even if we change the lst elements
    lst=[10,20,30]
    print(id(lst))
    updateList(lst)
    print("lst: ",lst)