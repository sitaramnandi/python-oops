import functools
def addop(a,b): #normal function
     return a+b
# main program
lst=[10,20,30,40,50]
res=functools.reduce(addop,lst)
print("Sum({})={}".format(lst,res))

# or
import functools
lst=[10,20,30,40,50]
res=functools.reduce(lambda a,b:a+b,lst)
print("Sum ({})={}".format(lst,res))



