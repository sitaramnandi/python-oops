a=1
b=2
def fun1():
    global a,b
    a+=1
    b*=2

def fun2():pass

# main program
print("In main program before fun1 a={} and={}".format(a,b))
fun1()
print("In main program before fun1 a={} and={}".format(a,b))
