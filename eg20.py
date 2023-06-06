import demo
# here we will learn about the concept of __name__
# since we have imported demo , firstly demo.py code will get executed
# so if we don't want to execute the code of demo, so we will write the code of demo.py inside a function
print("Inside eg20.py: "+__name__) # it will print __main__
# we have also created demo.py to understand this concept

