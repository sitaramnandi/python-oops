class Employee:
    @classmethod
    def getcompany(cls):
       cls.cname="TCS-HYD"
    def readempdata(self):
        try:
          self.eno=int(input("Enter the Emp ID:"))
          self.ename=input("Enter The Emp Name:")
          self.sal=float(input("Enter The salary:"))
        except ValueError:
           print("Do not Enter the str nd any specisl symbol")

    def  dispempdata(self):
       Employee.getcompany() #calling class level method
       print("EmployeeID:{}".format(self.eno))
       print("Employee name={}".format(self.ename))
       print("Employee Salary={}".format(self.sal))
       print("Employee Company Name={}".format(self.cname))   #calling class methid w.r.t self


# main progbram
e1=Employee()
e2=Employee()
print("-"*50)
print("Enter The first Emp Detalis")
e1.readempdata()
print("-"*50)
print("First Employee Detalis")
e1.dispempdata()
print("-"*50)
print("Enter The second Emp Detalis")
e2.readempdata()
print("-"*50)
print("Second Employee detalis")
e2.dispempdata()
print("-"*50)