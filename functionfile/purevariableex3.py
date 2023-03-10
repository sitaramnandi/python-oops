def disp(*param): # here * param is called var leg parameter and type tupple 
     # print(param,type(param))
     print("-"*50)
     print("Number of values=",len(param))
     for val in param:
          print("{}".format(val),end=" ")
          print()
# main program
disp(10) #function call-1
disp(10,20) #fumction call-2
disp(10,20,30,40) #function call-3
disp(10,20,30,40,50,60,"KVR")
disp()