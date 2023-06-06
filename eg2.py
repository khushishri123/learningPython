import sys
def inputExamples():
    # here we learn how to take inputs in python, input function always return string type
    # x will be assigned a string
    x = input("Enter first number")
    print(type(x))
    y = input("Enter second number")
    print(x + y)  # output will be 2312,it will concatenate string
    a=int(x)
    b=int(y)
    z=a+b
    print(z) # now its output will be the addition
    # fetching a character, we may type s string and input function will take the entire string too . But since we have written
    # [0], it will assign only first letter to ch
    ch=input("Enter a char: ")[0]
    print(ch)
    # now if we are providing an expression and we want to evaluate it,then
    result=eval(input("Enter expression: "))
    print(result)





if __name__ == '__main__':
    inputExamples()