import sys
def mutipleArgumentsFromConsole():
    # now if you want to pass multiple values from console, you can pass it but you need to import sys for using argv
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(x + y)
    # generally we give 4 spaces , 1 tab= 4 spaces



if __name__=="__main__":
    mutipleArgumentsFromConsole()