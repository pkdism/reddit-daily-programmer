def add1_string(num):
    res = ""
    return res.join([res + (str(int(i) + 1)) for i in str(num)])

print(add1_string(9))
print(add1_string(998))
