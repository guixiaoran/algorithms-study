def romanToInt(self, s: str) -> int:
    result = 0
    for i in range(len(s)):
        if s[i] == 'I':
            result += 1
            if i + 1 < len(s) and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                result -= 2
        elif s[i] == 'V':
            result += 5

        elif s[i] == 'X':
            result += 10
            if i + 1 < len(s) and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                result -= 20
        elif s[i] == 'L':
            result += 50

        elif s[i] == 'C':
            result += 100
            if i + 1 < len(s) and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                result -= 200
        elif s[i] == 'D':
            result += 500
        else:
            result += 1000

    return result