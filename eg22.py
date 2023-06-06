class Person:
    # creating instance variable
    nationality="Indian"

    def __init__(self,age,name):
        self.age=age
        self.name=name
        self.mam=self.Mammal()
    # tom and compare are non static methods because we are passing self. They will run differently for a particular object
    # whenever you are working with class variable ,the first parameter will be cls instead of self also you have to make
    # use of decorator :  @classmethod, for eg: see method getNationality
    def tom(self):
        print("Hi, I am tom")
        # print(self.age)
        # print(self.name)

    def compare(self,other):
        if self.age==other.age:
            print("Belong to same age group")
        else:
            print("Belong to different age group")

    #A class method can access or modify the class state while a static method can’t access or modify it.
    @classmethod
    def getNationality(cls):
        return cls.nationality

    # there is one another method known as staticmethod ,which has nothing to do with instance variable, or class variable
    @staticmethod
    def info():
        print("THis is just a static method")


    class Mammal:
        def display(self):
            print("Its a mammal")



if __name__=="__main__":
    # here we will create class and oject
    # to create object
    a=Person(20,"Kajal")
    a.tom()
    # or we can also call dog method by writing :
    Person.tom(a) # generally
    a2=Person(23,"Ram")
    a.compare(a2)
    # to change the value of static or class variable
    Person.nationality="German"
    # to access
    print(a.nationality)
    print(Person.getNationality())
    Person.info()
    # accessing inner class method
    a.mam.display()

    #Inheritance concept: Let suppose there is a class named as A and there is some another class named as 'B'. B want to
    # inherit 'A' . For that we have to write class B(A)




