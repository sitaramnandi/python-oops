# find the squre of the number from the list by applying map()
num=lambda n:n**2
lst=[10,-5,3,7,6,8,-11]
sqlst=list(map(num,lst))

print("*"*50)
print("GivenElement Squre")
for gn,sq in zip(lst,sqlst):
     print(gn,"-->",sq)
