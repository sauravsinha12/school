import pickle
def insertR():
    fo=open("Student1.dat","ab")
    roll=int(input("Enter your roll no"))
    name=input("Enter your name")
    marks=float(input("Enter your Marks"))
    rec=[roll,name,marks]
    pickle.dump(rec,fo)
    fo.close()
def disp():
    with open("Student1.dat","rb") as fi:
        count=0
        try:
            while True:
                rec=pickle.load(fi)
                print("Roll no ",rec[0])
                print("Name   ",rec[1])
                print("Marks  ",rec[2])
                print(" =================================")
                count+=1
        except:
            if count==0:
                print("No record")
            else:
                print(count,"   Record printed")
def search(roll):
    with open("Student1.dat","rb") as fi:
        count=0
        try:
            while True:
                rec=pickle.load(fi)
                if int(rec[0])==int(roll):
                    print("Roll no ",rec[0])
                    print("Name   ",rec[1])
                    print("Marks  ",rec[2])
                    print(" =================================")
                    count+=1
        except:
            if count==0:
                print("No record")
            else:
                print(count,"   Record printed")
print("\t\tMain Menu\nPress 1 to insert\nPress 2 to Display\nPress 3 to Search\nPress 6 to Exit")
while True:
    ch=int(input("Enter your choice "))
    if ch==1:
        insertR()
    elif ch==2:
        disp()
    elif ch==3:
        r=int(input("Enter the roll number be searched "))
        search(r)
    elif ch==6:
        print("Good bye")
        exit()
        

