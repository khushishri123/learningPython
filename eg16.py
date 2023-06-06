if __name__=="__main__":
    # here we will learn about anonymous function or lambda
    # remember functions are objects in python
    # so the syntax of creating a lambda function is:
    # lambda a- > a is parameter of that anonymous function , a*a is the operation
    #remember lambda can be used when the function contains only single line
    f= lambda a: a*a
    sum=lambda a,b: a+b

    x=f(5)
    print(x)

    s=sum(3,5)
    print(s)

