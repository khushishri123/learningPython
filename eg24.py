class Pycharm:
    def execute(self):
        print("Running")
        print("Printing")

class MyEditor:
    def execute(self):
        print("Spell checking")
        print("Running")
        print("Printing")

class Laptop:
    def code(self,ide):
        ide.execute()

if __name__=="__main__":
    # here we will learn about polymorphism
    # There are 4 ways : Duck typing, method overloading, method overriding ,operator overloading
    # here we will learn about duck typing
    # It is quite similar with interfaces in Java
    l=Laptop()
    # duck typing means it does not matter which class object does we pass ,it can of Pycharm or it can be of MyEditor,
    # the thing which matters is that it should contins execute method
    # If there is a bird, it behaves like a duck, quack likes a duck, swims like a duck, it can be a duck.
    l.code(Pycharm())


