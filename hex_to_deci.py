while True:
    try:
        a = input()  # 0xABCD
        ans = 0
        digit = 0
        while len(a) > 2+digit:
            temp = a[-1-digit]
            if temp == 'A':
                temp = 10
            elif temp == 'B':
                temp = 11
            elif temp == 'C':
                temp = 12
            elif temp == 'D':
                temp = 13
            elif temp == 'E':
                temp = 14
            elif temp == 'F':
                temp = 15
            temp = int(temp)
            temp = temp * (16 ** digit)
            ans = ans + temp
            digit += 1
        print(ans)
    except:
        break