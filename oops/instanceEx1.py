# program for reading and dispaly the Employee data by using classes and object who are working in same company by using instance method

class Employee:
    def readempdata(self):
        print("Id of current object={}".format(id(self)))


# main program
e1=Employee()   #object creation
e2=Employee()  #object creation
print("Id of e1 in main program=",id(e1),type(e1))
e1.readempdata() 
print("Id of e2 in main program=",id(e2),type(e2))
e2.readempdata()









