if __name__=="__main__":
    # Here we will learn about generators
    # generators give us iterators , here instead of return we will use yield. yield will return next value.Unlike return
    # statement, it is not necessary to write yield in last line. See code:
    def token():
        n=1
        # we will return squares of first 10 numbers
        while n<=10:
            sq=n*n
            yield sq
            n+=1

    t=token()
    for i in t:
        print(i)
