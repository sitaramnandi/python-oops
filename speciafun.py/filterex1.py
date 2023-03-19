def posfun(n):
    if n>0:
        return True
    else:
        return False
def negfun(n):
    if n<0:
        return True
    else:
        return False
# main function
lst=[10,-23,34,55.55,-90,66,-4]
filterobj1=filter(posfun,lst)
filterobj2=filter(negfun,lst)
poslist=list(filterobj1)
neglist=tuple(filterobj2)
print("Given list of values:{}".format(lst))
print("Positive elements:{}".format(poslist))
print("Negative list:{}".format(neglist))

