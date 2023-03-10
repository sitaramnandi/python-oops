# This program is not execute bz  Pvm is interpretor and it reamber only lastest function definiton  but not able to  rember all the defination bz all the function name is same
def disp(a): #function defination-1
    print(a)
disp(10) #function call-1
print("-"*50)
def disp(a,b):  #function defination-2
     print(a,b)
disp(10,20) #fumction call-2
print("-"*50)
def disp(a,b,c):  #function defination-3
     print(a,b,c)
disp(10,20,30)  #function call-3
print("-"*50)
def disp(a,b,c,d):  #function defination-4
     print(a,b,c,d)
disp(10,20,30,40)  #function call-4
print("-"*50)
def disp():
     print("MNot Taking")
disp() #function call 5
# In The above program we have 5 function calls and 5 function def.
#   1000 function calls--1000 function defs  time consuming
#  Today with var length args concept
# we have 10000 function calls-1def