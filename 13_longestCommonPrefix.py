def longestCommonPrefix(strs) -> str:
    if len(strs) < 1:
        return ""
    if len(strs) == 1:
        return strs[0]
    min = 100
    for i in range(len(strs)):
        if len(strs[i]) < min:
            min = len(strs[i])
    outlen = 0
    for i in range(0, min):
        outlen += 1
        for j in range(1, len(strs)):
            if strs[j - 1][i] != strs[j][i]:
                outlen -= 1
                if outlen > 0:
                    return strs[0][:outlen]
                else:
                    return ""

    if outlen > 0:
        return strs[0][:outlen]
    else:
        return ""
a = ["aflower","flow","flight"]
print(longestCommonPrefix(a))