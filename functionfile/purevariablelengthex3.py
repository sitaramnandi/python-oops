# program for finding sum of variable length argument
def findsum(sno,sname,*sum): # here * param is called var leg parameter and type tupple 
     print("-"*50)
     print("Student Number={}".format(sno))
     print("Student name={}".format(sname))
     print("-"*50)
     s=0
     for val in sum:
          print("{}".format(val),end=" ")
          s=s+val
     print()
     print("Sum={}".format(s))
     print("-"*50)
# main program
findsum(1,"RS",10) #function call-1
findsum(2,"Wk",10,20) #fumction call-2
findsum(3,"KVR",10,20,30) #function call-3
findsum(4,"ZS",10,20,30,4.4) #function call-4
