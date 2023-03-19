import functools
tpl=("Rossum","is","the","father","of","Python")
res=functools.reduce(lambda a,b:a+" "+b,tpl)
print("Result=",res)
