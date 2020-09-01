def find(a):
    max=0
    for i in range(len(a)):
        table = [0] * 800
        l = 0
        for j in range(i, len(a)):
            # longest substring without repeated char starts from this charcter
            if table[ord(a[j])] != 0:
                if l > max:
                    max = l
                break
            else:
                table[ord(a[j])] += 1
                l += 1
        if l > max:
            max = l
    return max






a= "!@#$%^&*"
print(find(a))