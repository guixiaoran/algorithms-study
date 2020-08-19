#分解质因数
#
# 读入一个数字
# 创建一个output list
# 从2开始，找整除数
#

while True:
    try:
        a = int(input())  # 0xABCD
        outlist=[]
        i=2
        while i <= a:
            if a%i == 0:
                outlist.append(i)
                a//=i
                i-=1
            i+=1

        for i in range(0,len(outlist)):
            print(outlist[i],end=" ")

    except:
        break