# find postive list and negtive list from thr list applying filter of function
poslst=lambda n:n<0
neglst=lambda n:n>0

# main program
lst=[10,-299,30,-8,88,33,-55,100]
newpos=list(filter(poslst,lst))
newneg=tuple(filter(neglst,lst))
print("Positive list={}".format(newpos))
print("Negitive list={}".format(newneg))

