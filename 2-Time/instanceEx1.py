class Employee:
    cname="TCS"
    



# main program
e1=Employee()   #object creation
# e2=Employee()

e1.eno=int(input("Enter the Emp ID:"))
e1.Ename=input("Enter the emp Name:")
e1.sal=float(input("Enter The Salary:"))
print("First Employee detalis")
print(e1.eno,e1.Ename,e1.sal,Employee.cname)
# print(e1.__dict__)


