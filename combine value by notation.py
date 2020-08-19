f= open('input.txt',"r")
a=[]
for line in f:
    a.append(line.split(" "))
print(a)

ma=0
for i in range(1,int(a[0][0])+1):
    if int(a[i][0])> ma:  # max index
        ma = int(a[i][0])
print(ma)

# create a list with size ma
out = [0]*(ma+1)
print(out)

# fill values correspond to its lable as index
for i in range(1,len(a)):
    ind=int(a[i][0])
    val=int(a[i][1])
    out[ind]+=val

for i in range(len(out)):
    if out[i] != 0:
        print(str(i)+" "+str(out[i]))









