class Employee:
     @classmethod
     def getempname(cls):
         cls.cname="TCS"
         cls.getempadr() #calling class level method w.r.t cls
     @classmethod
     def getempadr(cls):
         Employee.addr="HYD"
     def readempdet(self):
          try:
            self.eid=int(input("Enter The Employee ID:"))
            self.ename=input("Enter The Emp Name (Enter A valid Name):")
            self.esal=float(input("Enter The salary:"))
          except ValueError:
              print("Do not Enter THE str and Any special Symbol")
     def disempdet(self):
        Employee.getempname()  #calling class method
        print("Employee ID:{}".format(self.eid))
        print("Employy Name:{}".format(self.ename))
        print("Employee salry:{}".format(self.esal))
        print("Company NAme:{}".format(Employee.cname))  #calling class level method w.r.t class name
        print("Address of Company:{}".format(self.addr)) #calling class level method w.r.t self
class disp:
     
     @staticmethod
     def disobjectdata(obj):
          for k,v in obj.__dict__.items():
               print("{}-->{}".format(k,v))




# main program
e1=Employee()
e2=Employee()
print("Enter First Employee Detalis:")
e1.readempdet()
print("-"*50)
print("First Employee detalis")
disp.disobjectdata(e1)
print("-"*50)
print("Enter Second Employee Detalis:")
e2.readempdet()
print("SEcond Employee Deatlis")
disp.disobjectdata(e2)
