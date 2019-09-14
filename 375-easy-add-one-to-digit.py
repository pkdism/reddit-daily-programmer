def add1_string(num):
    s = str(num)
    res = ""
    for i in s:
        j = int(i)
        k = str(j + 1)
        res += k
    return res



print(add1_string(9))
print(add1_string(998))
