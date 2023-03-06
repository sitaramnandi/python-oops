class Student:
    @classmethod
    def getadd(cls):
         cls.addr="HYD"
    def readstuddata(self):   #instance method
          self.sno=int(input("Enter The Student No:"))
          self.sname=input("Enter The Student Name:")
          self.smark=float(input("Enter The mark:"))
        
class Employee:
     def readempdata(self): #instance method
          self.eno=int(input("Enter The Employee ID:"))
          self.ename=input("Enter The Employee Name:")
          self.esal=float(input("Enter Employee salary:"))

class Teacher:
    def readteachdata(self): #instance method
         self.tno=int(input("Enter The Teacher Id:"))
         self.tname=input("Enter teacher name:")
         self.tsub=input("Enter The Teacher Subject:")
         
class Hyd:
     Student.getadd()
     @staticmethod
     
     def disobjectdata(obj):
          for k,v in obj.__dict__.items():
               print("{}-->{}".format(k,v))

          print("Addres={}".format(Student.addr))

# main program
s=Student()  #object creation
e=Employee()  #object creation
t=Teacher()   #object creation
# reading Student data
s.readstuddata()  #calling instance method
e.readempdata()  #calling instance method
t.readteachdata()  #calling instance method
# dispaly Student data
print("-"*50)
print("Student Detalis")
print("-"*50)
Hyd.disobjectdata(s)
print("-"*50)
# dispaly Teacher data
print("Employee Detalis")
print("-"*50)
Hyd.disobjectdata(e)
print("-"*50)
# dispaly teacher data
print("Teacher Detalis")
Hyd.disobjectdata(t)