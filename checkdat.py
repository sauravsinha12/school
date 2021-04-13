import pickle
"""with open("Dat.dat","ab") as fo:
    roll=int(input("Enter your roll number"))
    name=input("Enter your name")
    rec=[roll,name]
    pickle.dump(rec,fo)"""
with open("Dat.dat","rb") as fi:
    try:
        while True:
            rec=pickle.load(fi)
            for i in rec:
                print(i,end=" ")
            print()
    except:
        print("End")
    
