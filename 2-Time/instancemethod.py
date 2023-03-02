class Student:
     sname="T.G HIGH SCHOOL"
     def readstdata(self):   #instance method
          try:
               self.sno=int(input("Enter The Student Id:"))
               self.sname=input("Enter The Student Name:")
               self.mark=float(input("Enter Mark:"))
          except ValueError:
               print("Do Not Enter The Str And Eny Special Symbol")
     def disstdata(self):
          print("student ID={}".format(self.sno))
          print("student Name={}".format(self.sname))
          print("student mark={}".format(self.mark))
          print("School Name={}".format(Student.sname))
     
        


# main program
s1=Student()   #object creation
s2=Student()    #object creation
print("-"*50)
print("Enter The First student data")
s1.readstdata()
print("-"*50)
print("First student Detalis")
s1.disstdata()
print("-"*50)
print("Enter The second student data")
s2.readstdata()
print("-"*50)
print("scond student Detalis")
s2.disstdata()
print("-"*50)

