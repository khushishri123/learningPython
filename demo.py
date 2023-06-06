
def main():
    print("Hello",end=" ")
    print(__name__) # if we will execute demo.py then it will print __main__ but once we will import demo as package in
    # eg20.py , and if we execute eg20.py , it will show demo instead of __main__

if __name__=="__main__":
    main()
    # so this is the trick , main() function will get exceuted only when __name__ ==="__main__". if demo.py is used as a library
    # we don't want to execute main

