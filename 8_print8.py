f= open('input.txt',"r")
a=[]
for line in f:
    a.append(line)
la = a[1]
lb = a[0]

#case 1: len()>8
i=0
while i <= len(la)-8:
    print(la[i:i+8])
    i+=8

if i< len(la):
    print(la[i:len(la)-1]+'0'*(8-len(la)+i+1))

i=0
while i <= len(lb)-8:
    print(lb[i:i+8])
    i+=8

print(lb[i:len(lb)-1]+'0'*(8-len(lb)+i+1))
