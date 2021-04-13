fo=open("9april.dat","rb+")
name=input("Enter your name")
fo.seek(0)
fo.write(bytes(name,'utf8'))
fo.close()

"""
fo=open("9april.dat","rb")
fo.seek(10)
data=fo.read()

print(data)

fo.close()"""
