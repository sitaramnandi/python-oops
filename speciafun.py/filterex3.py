# program for filtering element from given list of element
line=input("Enter The line of text:")
vwlst=list(filter(lambda a:a.lower() in ["a","i","o","u","e"] and a.isalpha,line))
print(vwlst)