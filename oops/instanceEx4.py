
class Employee:
     def readempdata(self):   #instance method
          try:
               self.eno=int(input("Enter the Employee ID:"))
               self.ename=input("Enter The Student Name:")
               self.sal=float(input("Enter The salary:"))
          except ValueError:
                    print("Do not Enter ste and any special symbol")
     def dispempdata(self): #instance method

          print("Employee number={}".format(self.eno))
          print("Employee name={}".format(self.ename))
          print("Employee salary={}".format(self.sal))



# main program
e1=Employee()
e2=Employee()
# reading Employee data
print("Enter the First Employee detalis")
e1.readempdata()
# reading Second Employee detalis
print("Enter Second Employee detalis")
e2.readempdata()
print("-"*50)
print("First Emp Detalis")
e1.dispempdata()
print("-"*50)
e2.dispempdata()
print("Second Emp data")
