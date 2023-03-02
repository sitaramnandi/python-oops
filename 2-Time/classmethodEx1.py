class Employee:
    @classmethod
    def getcomdet(cls):
           cls.cname="Wipro"
    def readempdata(self):
        self.eno=int(input("Enter the Emp ID:"))
        self.ename=input("Enter the Emp NAme:")
        self.sal=float(input("Enter The salary:"))
    def  dispempdata(self):
        self.getcomdet()
        print("Employee ID={}".format(self.eno))
        print("Employee name={}".format(self.ename))
        print("Employee Salary={}".format(self.sal))
        print("Company Name={}".format(Employee.cname))
# main program
e1=Employee()
e2=Employee()
# reading Employee data
print("Enter The First Employee Data")
e1.readempdata()
print("-"*50)
e1.dispempdata()
print("-"*50)
#  reading Employee data
print("Enter The Seocnd Employee Data")
e2.readempdata()
print("-"*50)
e2.dispempdata()
print("-"*50)


