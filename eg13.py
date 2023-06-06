


if __name__=="__main__":
    # here we will learn about the concept of global variable

    a =10 # global variable
    print("Id of global a: ",id(a))
    def tom():
        a=12 # local variable
        # inside function , preference will be always given to local variable
        # if there is not local variable named as 'a' we can access the global variable inside the function
        # but as soon as we will assign it a new value it will create local variable named as a
        print("inside tom function: ",a)

    def sam():
        # here we want to change the value of global variable , but as soon as we will change the value of a it will assign
        # new memory block for a, hence creating a local variable. But we want to change the value of global a, so we
        # have to tell python that treat that as global variable, for that we have to declare a with global keyword
        global a
        a=15 # it will change the global variable value too
        print("Inside sam function: ",a)
        # but once you declared a variable global , you cannot create a local varibale named as a
        # so we will not use the concept of global keyword, so for the final solution see function jack

    def jack():
        # we will learn about globals function. Actually we just want to access the address of global variable.
        x=globals()['a'] # there can be so many global valriables so we have to specify which global variable does we want
        print("Value of x: ",x)
        print("Id of x: ",id(x)) # id of x and global a will be same
        # remember don't change the value of x, if you will change the value of x, it will create a new local variable named as x
        # to change the value of global variable ,write:
        globals()['a']=21
        a=9




    tom()
    # remember you cannot access the local varibale outside the function
    #sam() # see sam function also
    jack()
    print("Outsider function: ",a)





