if __name__=="__main__":
    # here we will learn about zip function. It can zip 2 lists into a dict or a set or another list
    l1=[3,23,12,44,55,90,100]
    l2=["Ram","Shyam","Gita","Sita","Tom","Harry","Jack"]
    zipped=zip(l1,l2)
    for (a,b) in zipped:
        print(a," ",b)

    mpp=dict(zip(l1,l2))
    print(mpp)

    st=set(zip(l1,l2))
    print(st)