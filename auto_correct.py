
def deletechar(string,ind):
    string = string[0:ind]+string[ind+1:]
    return string
def check(s):
    if len(s) > 2:# situation 1
        j=0
        while j < len(s)-2:
            if s[j] == s[j + 1]:
                front = s[j]
                k = j
                while k + 2 < len(s) and s[k + 2] == front:
                        s= deletechar(s, k + 2)
            j += 1
            # situation2
        for k in range(len(s) - 3):
            if s[k] == s[k + 1]:
                front = s[k + 2]
                while k < len(s) - 3 and front == s[k + 3]:
                    s = deletechar(s, k + 3)
    return s


s = 'helllo'
print(check(s))
