class Student:
    def __init__(self,age):
        self.age=age


    def __add__(self, other):
        age=self.age+other.age
        s=Student(age)
        return s

    def __gt__(self, other):
        if self.age>other.age:
            return True

        else:
            return False

    def __str__(self):
        return self.age

if __name__=="__main__":
    # here we will learn about operator overloading
    # for overloading an operator we have different methods such as __add__ , __gt__
    s1=Student(12)
    s2=Student(22)
    s3=s1+s2
    # whenever we try to print value ,then internally __str__() method is called
    # the moment we try to print the values of s1,it will not print the values of s1,instead it will print the address
    # you have to override this method __str()__, for returning the value of s3
    print(s3.__str__())
    if s1.__gt__(s2):
        print("Greater than")
    else:
        print("Smaller")

        # to attach int in string: '{} {}'.format(a1,a2).Here in place of Null , we have None


