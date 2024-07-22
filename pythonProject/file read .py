#f=open("vassu.txt")
#print(f.seek(4))
#print(f.read())
#another method

myfile=open("vassu.txt")
vlist=list("aeiouAEIOU")
vc=0
x=myfile.read()
for y in x:
if(y in vlist):
vc+=1
print(vc)