class student:
    pass

# main program
s1=student()  #object creation
s2=student()
s1.sno=10
s1.sname="Rs"
s1.mark=34.55
s2.stno=20
s2.name="Tr"
s2.marks=55.55
# dispaly the data of s1 object
print("Content of s1")
print(s1.sno,s1.sname,s1.mark)  
# dispaly the dsata of s2 by object
print("Content of s2")
print(s2.stno,s2.name,s2.marks)
print("------------------OR----------------------")
for k,v in s1.__dict__.items():
    print("{}-->{}".format(k,v))
print("content of s2")
for k,v in s2.__dict__.items():
     print("{}-->{}".format(k,v))