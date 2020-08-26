"""
写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，
然后输出输入字符串中含有该字符的个数。不区分大小写。

第一行输入一个有字母和数字以及空格组成的字符串，第二行输入一个字符
输出输入字符串中含有该字符的个数。

a=input().lower()
b=input().lower()
print(a.count(b))

"""
def cal(target, thestr):
    # create a list with size of all char and numbers and blank
    # 26+10+1
    out=[0]*37
    for i in range(len(thestr) - 1):
        if thestr[i].isnumeric() == True:
            out[int(thestr[i])] += 1
        elif thestr[i].isnumeric() == False:
            if thestr[i]== " ":
                out[10]+=1
            else:
                if thestr[i].isupper():
                    out[ord(thestr[i]) - 54] += 1
                else:
                    out[ord(thestr[i]) - 86] += 1

    if target.isnumeric() == True: # number
        return out[int(target)]
    elif target.isnumeric() == False:
        if target == " ":
            return out[10]
        else:
            if target.isupper():
                return out[ord(target) - 54]
            else:
                return out[ord(target) - 86]


f= open('input.txt',"r")
a=[]
for line in f:
    a.append(line)
target = a[1]
thestr = a[0]
#print(target)
#print(thestr)
#print(ord('A')) # a 97 A 65
print(cal(target, thestr))

