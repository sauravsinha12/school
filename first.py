number=[10,20,25,30]
length=10
try:
    if length>len(number):
        raise IndexError
        print("No Execution")
except IndexError:
    print("Your division is not proper")
