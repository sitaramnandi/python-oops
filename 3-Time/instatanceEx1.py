class Employee:
    cname="TCS"




# main program
e1=Employee() #Object creation
e2=Employee() #object Creation

e1.eid=int(input("Enter The Emp ID:"))
e1.ename=input("Enter The Emp Name:")
e1.sal=float(input("Enter The salary"))
print("-"*50)
# print(e1.__dict__)
print("First Employee detalis:")
print("Employee id:{}".format(e1.eid))
print("Employee Name={}".format(e1.ename))
print("Employee salary={}".format(e1.sal))
print("Company Name={}".format(Employee.cname))

print("-"*50)
e2.eid=int(input("Enter The Emp ID:"))
e2.ename=input("Enter The Emp Name:")
e2.sal=float(input("Enter The salary"))
print("-"*50)
# print(e2.__dict__)
print("Second Employee detalis:")
print("Employee id:{}".format(e2.eid))
print("Employee Name={}".format(e2.ename))
print("Employee salary={}".format(e2.sal))
print("Company Name={}".format(Employee.cname))