v=input("enter your file name")
a=input("enter your second file name")

with open(v,'r') as f:
    date_f=f.read()
#f.read indicates you are reading the file and storing it in the variable data_f. Now all gthe file contents is stord in the variable data_f

with open(a,'r') as s:
    date_s=s.read()

with open(v,"w") as f:
    f.write(date_s)

with open(a,'w')as s:
    s.write(date_f)
