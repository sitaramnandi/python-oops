def dispstdata(sid,sname,smark,crs="Python"):
     
    print("Student id={}".format(sid))
    print("Student name={}".format(sname))
    print("Student Mark={}".format(smark))
    print("Course={}".format(crs))


# main program
try:
    print("Enter First student Detalis")
    a=int(input("Enter The Student ID:"))
    b=input("Enter The student name:")
    c=float(input("Enter The student mark:"))
    print("Enter The second emp detalis")
    x=int(input("Enter The Student ID:"))
    y=input("Enter The student name:")
    z=float(input("Enter The student mark:"))
except ValueError:
    print("Do not Enter The str and any special symbol")
dispstdata(a,b,c)

dispstdata(x,y,z)