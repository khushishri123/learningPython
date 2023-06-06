class TopTen():
    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration

if __name__=="__main__":
    # we will learn about iterables
    # there is a method called iter() which will give us t
    # the object of iterables ,next() which will give us the next value
    nums=[7,0,9,8,12]
    it=iter(nums)
    print(type(it))
    print(it.__next__())

    t=TopTen()
    print(t.__next__()) # it will print 1 and because we have called __next()__ it will do num++, so the below for loop will
    # start from 2
    for i in t:
        print(i)

