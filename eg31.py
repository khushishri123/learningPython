from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(1,20):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(1,20):
            print("Hi")
            sleep(1)

if __name__=="__main__":
    t1=Hello()
    t2=Hi()
    t1.start()
    sleep(0.5)
    t2.start()
    # we have called join method so that main thread will not end untill t1 thread completes its execution
    t1.join()
    t2.join()
    print("Bye!!")
