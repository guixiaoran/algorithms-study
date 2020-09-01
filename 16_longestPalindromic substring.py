'''
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

or abbc output bb

"a" -> a
"bb" -> bb
"aaaa" -> aaaa
'''


def longestPalindrome(s) -> str:
    maxlen = 0
    p = ""
    if len(s) < 3:
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        elif len(s) == 1:
            return s
        else:
            return ''
    for i in range(1,len(s)):
        if (i+1) < len(s) and s[i-1] == s[i+1]:# aba
            t = 1
            temp = 1
            while (i-t)>=0 and (i+t)<len(s) and s[i-t] == s[i+t]:
                temp+=2
                t+=1
            if temp > maxlen:
                maxlen = temp
                p = s[i-t+1:i+t]

        if (i+1) < len(s) and s[i] == s[i+1]: # abba
            t = 1
            temp = 2
            while (i - t) >= 0 and (i + 1 + t) < len(s) and s[i - t] == s[i + 1 + t]:
                temp += 2
                t += 1
            if temp > maxlen:
                maxlen = temp
                p = s[(i - t + 1):(i + t+1)]
        elif s[i-1] == s[i]:
            temp = 2
            if temp>maxlen:
                maxlen = temp
                p=s[i-1:i+1]


    if maxlen ==0:
        return s[0]
    return p

a="ababd"
print(longestPalindrome(a))
