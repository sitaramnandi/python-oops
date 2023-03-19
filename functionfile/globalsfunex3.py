a=10
b=20

def opertion():
     d=globals()
#     print(d)
     print("-"*50)
     for gn,gv in d.items():
        print("{}-->{}".format(gn,gv))
     print("-"*50)
     print("Programerv defined global variable name and values type-1")
     print("Global var a=",d["a"])
     print("Global var a=",d["b"])
     print("="*50)
     print("Programerv defined global variable name and values type-2")
     print("Global var a=",d.get("a"))
     print("Global var a=",d.get("b"))
     print("="*50)
     print("Programerv defined global variable name and values type-3")
     print("Global var a=",globals()["a"])
     print("Global var a=",globals()["b"])
     print("="*50)
     print("Programerv defined global variable name and values type-4")
     print("Global var a=",globals().get("a"))
     print("Global var a=",globals().get("b"))



     



# main program
opertion()
