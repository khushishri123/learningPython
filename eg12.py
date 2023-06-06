def person1(name,age=21):
    print(name)
    print(age)

# in c++ , we have the option of ..., but in pythin its *
def sum(a,*b):
    print(a)
    print(b)
    c=a
    for i in b:
        c+=i
    print(c)


def personData(name,**data):
    print(name)
    print(data)



if __name__=="__main__":
    # now we will learn about different types of arguments
    #keyword argument, in which we will write the name of the argument while passing its value
    person1(age=28,name="Ram")
    #default arg, in which if we didn't pass the value to the argumnet then a defualt value will be assigned to it
    person1("Sita")
    # variable length output   , in which we can pass any number of arguments
    sum(10,20,30,40)
    # keyword varaible length arguments, if you are passing without keyword then write *data but if you are passing keyword
    # names too then write **data
    personData('RamSita',age=23,city="Ayodhya",mobile=743749389)
