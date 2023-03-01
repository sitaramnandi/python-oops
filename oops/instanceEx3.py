class Employee:
     
          def readempdata(self):  # instance method
               try:
                    self.eno=int(input("Enetr Employee No: "))
                    self.ename=input("Enter Employee Name")
                    self.sal=float(input("Enter The salary:"))
               except ValueError:
                    print("Do not enter the str and any special symbol")

# main program
e1=Employee()   #object creation
e2=Employee()  #object creation
#reading first employee Data
print("First Employee Detalis")
e1.readempdata() 
# reading second employee detalis
print("-"*40)
print("Second Employee Detalis")
e2.readempdata()
print("-"*50)
print(e1.__dict__)
print(e2.__dict__)

