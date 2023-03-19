# find min and max from from given list by applying reduce()
import functools
lst=[10,2000,130,240,50,-150]
maxv=functools.reduce(lambda a,b:a if a>b else b,lst)
minv=functools.reduce(lambda a,b: a if a<b else b,lst)
print("Max({})={}".format(lst,maxv))
print("Min({})={}".format(lst,minv))
