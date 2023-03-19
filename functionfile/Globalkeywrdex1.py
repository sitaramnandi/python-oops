a=10
def update1():
    global a
    a+=1
def update2():
     global a
     a*=2

# main program
print("val of global variable a in main program before update1():{}".format(a))
update1()
print("val of global variable a in main program after update1():{}".format(a))
update2()
print("val of global variable a in main program after update2():{}".format(a))