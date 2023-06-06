if __name__=="__main__":
    # here we will learn about decorators
    # DECORATORS ADD EXTRA FEATURES TO THE EXISTSING FUNCTION
    # you can change the existing behaviour of existing function
    # so lets suppose we want to divide a larger number by smaller number. But user can pass first smaller and then larger and
    # also we cannot change the definition of existing function div. So we will create a decorator

    def div(a,b):
        # this function is already created and we cannot change its definition or we cannot implement any condition
        print(a/b)

    # func is the div function itself
    def smart_div(func):
        # since div function has 2 parameters here also we have taken 2 parameters
        def inner(a,b):
            # here we will be writing the code that we want to wriote inside div function
            if a<b:
                a,b=b,a
            # here we are calling div only ,but by swaping the value of a and b
            return func(a,b)

        return inner

    # we are passing old div to smart_div and getting new div from smart_div, when we are calling div, so actually we are calling
    # new div

    div=smart_div(div)
    div(4,16)



