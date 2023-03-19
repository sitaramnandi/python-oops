# find the poslst and neg and the sum of poslst and neglst from the gievn list by applying filter and reduce

import functools
def readvalues():
    lst=[]
    n=int(input("Enter how many value u want:"))
    if n<=0:
        return lst
    else:
          print("Enter {} values".format(n))
          for i in range(1,n+1):
            lst.append(int(input()))
          return lst

# main program
lst=readvalues()
# [10,30,-40,100,399,44,-45]
if len(lst)==0:
    print("List is Empty and can not find sum of +ve and -ve values")
else:
     # filter applying  obtaing post and neg values
     poslst=list(filter(lambda n:n>0,lst))
     neglst=list(filter(lambda n:n<0,lst))
     sumposlst=functools.reduce(lambda a,b:a+b,poslst)
     sumneglst=functools.reduce(lambda a,b:a+b,neglst)
     print("Positive list of element={}".format(poslst))
     print("Negative list of element={}".format(neglst))

     print("Sum of Postive lst",sumposlst)
     print("Sum of neg lst=",sumneglst)
