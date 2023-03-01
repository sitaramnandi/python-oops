# program for reading and dispaly the Employee data by using classes and object who are working in same company by using instance method

class Employee:
     cname="TCS"
     


# main program
e1=Employee()
e2=Employee()
while True:
     try:
               # reading first employee detalis
          print(" Enter First Employee detalis")
          e1.eno=int(input("Enter The Emp No:"))
          e1.ename=input("Enter the Emp name:")
          e1.sal=float(input("Enter the salary:"))
          print("-"*50)
          # readung second employee detalis
          print(" Enter second Employee detalis")
          e2.eno=int(input("Enter The Emp No:"))
          e2.ename=input("Enter the Emp name:")
          e2.sal=float(input("Enter the salary:"))
          print("First Employee detalis")
          print("Employee number={}".format(e1.eno))
          print("Employee name={}".format(e1.ename))
          print("Employee salary={}".format(e1.sal))
          print("-"*50)
          print("Second Employee detalis")
          print("Employee number={}".format(e2.eno))
          print("Employee name={}".format(e2.ename))
          print("Employee salary={}".format(e2.sal))
          print("-"*50)
     except ValueError:
          print("Do not Enter the str and special symbol")