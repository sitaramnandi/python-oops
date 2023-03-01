class student:
    crs="Python" # class level data member  - inside the class def 

# main program
s1=student()
s2=student()
print("content of s1 before adding data={}".format(s1.__dict__))
try:
     s1.sno=int(input("Enter the Student number:"))
     s1.sname=input("Enetr the student name:")
     s1.smark=float(input("Enter the student mark:"))
     s2.stno=int(input("Enter the Student number:"))
     s2.name=input("Enetr the student name:")
     s2.mark=float(input("Enter the student mark:"))
     print("Content of s1")
     print(s1.sno,s1.sname,s1.smark,student.crs)   #accept w.r.t class name
     print("Content of s2")
     print(s2.stno,s2.name,s2.mark,student.crs)   #accept w.r.t class name

     print("-"*50)
     print("Content of s1")
     print(s1.sno,s1.sname,s1.smark,s1.crs)   #accept w.r.t object name
     print("Content of s2")
     print(s2.stno,s2.name,s2.mark,s1.crs)
except ValueError:
     print("Do not Enter the Str or any special symbol")

