# program for demostrating globalS()
a=10
b=20
c=10  #here a,b are called global variable
def opertion():
    a=100
    b=30
    c=30
    res=a+b+c+globals()["a"]+globals()["b"]+globals()["c"]
    print(res)
# main program
opertion()
# Note: In the above program we have different local variable and global variables 
