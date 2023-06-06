class A:

    def __init__(self):
        self.name="Khushi"
        print("Init of A")

    def dis(self):
        print("Hello,I am A")

class B():
# when you create object of sub classit will call init of sub class first.If you have called super then it will first call init
# of super class then call init of subclass
    def __init__(self):
        #super().__init__()
        self.age=21
        print("Init of b")

    def display(self):
        print("Hello,I am B")

#mutiple inheritance
class C(A,B):
    def __init__(self):
        # now for c THERE are 2 base classes A and B. So there is Method resolution ordrer in python which says that
        # we have to execute from left to right. So since A is on left, init of A will get executed
        super().__init__()
        print("Init of C")

if __name__=="__main__":
    # here we will learn about inheritance
    ob = B()
    ab = C()


