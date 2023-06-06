if __name__=="__main__":
    # here we will learn about file handling
    # there are generally 3 different modes to open a file: 'r','w','a'
    # But there are 2 other modes also: rb and wb. They are generally reading and writing content of an image. There are
    # 2 different types: character mode and binary mode. Binary mode is used to read image files.
    # reading a character file
    f=open('Calc.py','r')
    print(f)
    # to print entire data we use f.read()
    #print(f.read())
    # to print starting line we use readLine()
    #print(f.readline())
    f1=open('Myfile','w')
    # to write in a file
    #f1.write("Hello")
    # writing the entire content of f into f1
    for data in f:
        f1.write(data)

    # if we open a file in write mode it will be rewritten, to append data in file we have to open it in 'a' mode and the rest of
    # the syntax will be same as that of write
    # to open an image file in read mode we have to write:
    # f=open('IMG_PNG','rb') same thing for writing a image file: 'wb'


