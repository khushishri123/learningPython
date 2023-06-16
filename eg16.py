if __name__=="__main__":
    # here we will learn about anonymous function or lambda
    # remember functions are objects in python
    # so the syntax of creating a lambda function is:
    # lambda a- > a is parameter of that anonymous function , a*a is the operation
    #remember lambda can be used when the function contains only single line
    f= lambda a: a*a
    sum=lambda a,b: a+b

    x=f(5)
    print(x)

    s=sum(3,5)
    print(s)

    # we can also use lambda to sort a dict according to key or value
    dict_value={"apple":3,"cherry":2,"banana":1}
    # sorting according to the key
    # to sort according to the value just write : lambda x: x[1]
    sorted_list=sorted(dict_value.items(), key=lambda x : x[0])
    print(sorted_list)
    print(type(sorted_list))

    # to covert the above list into string

    items_as_strings = [f'{k}: {v}' for k, v in sorted_list]  # Create string representations
    print(items_as_strings)
    print('\n'.join(items_as_strings))  # Join strings with newline separator






