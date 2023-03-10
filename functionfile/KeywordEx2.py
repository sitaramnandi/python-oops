def dispstudinfo(sno,sname,mark,crs="Python"):
    print("\t{} \t{} \t{} \t{}".format(sno,sname,mark,crs))


# main program
print("-"*50)
print("\tsno \tsname \tmark \tcrs")
print("-"*50)
dispstudinfo(10,"RS",11.33)
dispstudinfo(30,mark=40,sname="TR",crs="Java")
# dispstudinfo(crs="war",sno="40",mark=44,sname="Putin")
dispstudinfo(sname="Joe",mark=55,sno=40)