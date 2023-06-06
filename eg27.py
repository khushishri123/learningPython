from abc import ABC,abstractmethod
class Calc(ABC):
    @abstractmethod
    def add(self,a,b):
        pass

class Add(Calc):
    def add(self,a,b):
        return a+b


if __name__=="__main__":
    # here we will learn about abstract class and method
    # there is a decorator: @abstractmethod and for using that method we have to import ABC,abstractmethod from abc,abc
    # means AbstractMethodClass. Also you have to declare that class as Abstract by writing : Calc(ABC)
    c=Add()
    print(c.add(10,10))
