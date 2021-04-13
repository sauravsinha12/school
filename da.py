import pickle
with open("New.dat","rb") as f1:
    rec=pickle.load(f1)
    print(rec)
fileout=open("student.dat","ab")
name=input("Enter your name")
fileout.write(bytes("\n"+name,'utf-8'))
fileout.close()

fileout=open("student.dat","r")
print(fileout.readlines())
fileout.close()
