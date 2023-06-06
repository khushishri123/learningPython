def count(lst):
    even=[]
    odd=[]
    for it in lst:
        if it%2==0:
            even.append(it)
        else:
            odd.append(it)
    return even,odd


if __name__=="__main__":
    # we want list of odd and even numbers
    lst=[12,13,88,65,78,100,99]
    even,odd=count(lst)
    print(even)
    print(odd)