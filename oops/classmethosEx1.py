class Employee:
    @classmethod
    def getcompdet(cls):
        Employee.cname="TCS-HYD"
          #   or
     #    cls.cname="TCS-HYD"

    def  readempdata(self):
          self.eno=int(input("Enter The Emp ID:"))
          self.ename=input("Enter The Emp name:")
          self.sal=float(input("Enter The Slary:"))

    def dispempdata(self):
     print("Employee ID={}".format(self.eno))
     print("Employee Name={}".format(self.ename))
     print("Employee Salry={}".format(self.sal))
     print("Company Name={}".format(self.cname)) # calling w.r.t self
     # print("Company Name={}".format(Employee.cname))   calling w.r.t class nname
       
# main program

e1=Employee()   #object creation
e2=Employee()  #object creation
Employee.getcompdet()

# raedemp Detalis
print("Enter First Emp Detalis")
e1.readempdata()
print("First Employee detalis")
e1.dispempdata()
print("*"*50)
# read second emp detalis
print("Enter Second Emp Detalis")
e2.readempdata()
print("Second Employee detalis")
e2.dispempdata()