def fibo():
    x=0
    y=1
    lst=[]
    while x<=34:
        lst.append(x)
        z=x+y
        x=y
        y=z
    return lst


def factorial(n):
    x=1
    for i in range(1,n+1):
        x=x*i

    return x


if __name__=="__main__":
    # we will print fibonacci series
    lst=fibo()
    print(lst)
    fact=factorial(5)
    print("factorial of 5: ",fact)