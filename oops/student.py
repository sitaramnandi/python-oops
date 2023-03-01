class student:
     pass

# main program
s1=student() #object creation
s2=student()
print("Content of s1 before adding add={}".format(s1.__dict__))  #{}
s1.sno=10
s1.sname="Rs"
s1.marks=56
print("Content of s1 after adding add={}".format(s1.__dict__))  #{'sno': 10, 'sname': 'Rs', 'marks': 56}
s2.stno=100
s2.name="TR"
s2.marks="ABC123"
s2.dob="22-12-2001"
print("Content of s1 after adding add={}".format(s2.__dict__)) 

