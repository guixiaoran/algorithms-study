def reverse(x):
    digit = len(str(x))
    result = 0
    # negative
    y = str(x)
    sign = 1
    if x < 0:
        sign = -1
        y = y[1:]
        digit -= 1
    # start from 0

    for i in range(digit):
        temp = int(y[0]) * (10 ** i)
        result += temp
        y = y[1:]
    #
    return result * sign

print(reverse(1534236469))