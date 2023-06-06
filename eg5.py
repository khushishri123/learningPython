def loopingExamples():
    i = 1
    while i <= 5:
        # let suppose we want to print in a single line with space,then write end=" "
        print("Khushi", end=" ")
        j=1
        while j<=3:
            print("Stuti",end=" ")
            j=j+1
        i = i + 1;
        # for changing the line
        print()
    #using for loop it will [rint from 0 to 9
    for i in range(10):
        print(i,end=" ")
    print()
    # when we want to specify starting,ending and interval
    for i in range(10,22,2):
        print(i,end=" ")
    print()

    # using for and else
    print("example of for and else: ")
    x=[12,23,46,34]
    for i in x:
        if i%5==0:
            print(i)
            break
    else:
        print("No number is divisible by 5")

    # there are keywords that are used inside a loop : break,continue, pass.
    # pass is generally used when we don't want to write a code inside a function or block.Like when you are defining a block and
    # you don't know what to write inside it, you can simply pass it


if __name__ == "__main__":
    loopingExamples()
