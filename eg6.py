def pattern1():
    for i in range(4):
        for j in range(4):
            print("#",end=" ")
        print()


def pattern2():
    for i in range(1,4,1):
        for j in range(i):
            print("#",end=" ")
        print()


def pattern3():
    for i in range(4,0,-1):
        for j in range(i):
            print("#",end=" ")
        print()



def printingPatterns():
    pattern1()
    print("------------------------")
    pattern2()
    print("------------------------")
    pattern3()


if __name__=="__main__":
    printingPatterns()