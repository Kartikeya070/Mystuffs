l=10 #global variable
def function1():
   # l=5 #local variable
    m=10
    global l
    z = l + 50
    print(l,m)
    print(z)
print(function1())
