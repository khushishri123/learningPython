if __name__=="__main__":
    # here we will learn about exception handling
    a=5
    b=0
    try:
        div=a/b
        print(div)

    except Exception as e:
        print(e) # e represents the exception

    finally:
        print("Finally block got executed")


