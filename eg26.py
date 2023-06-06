class Calc():
    # trying to implement method overloading indirectly
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a
        
    def show(self):
        print("Calc show method")
        
class Calc2(Calc):
    # method overriding
    def show(self):
        print("Calc2 show method")
if __name__=="__main__":
    #  python does not support method overloading.
    #  We may define many methods of the same name and different arguments, but we can only use the latest defined method
    # so we cannot directly implement method overloading but indirectly we can
    c=Calc()
    ans=c.add(12,13,14)
    print(ans)
    ans=c.add(12,12)
    print(ans)
    ans=c.add(12)
    print(ans)

    c2=Calc2()
    c2.show()

