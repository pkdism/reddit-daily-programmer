def add1_string(num):
    return ''.join(['' + (str(int(i) + 1)) for i in str(num)])

def add1_num(num):
    res = 0
    i = 0
    while num > 0:
        if num % 10 == 9:
            res = (100 ** i) + res
        else:
            res = (10 ** i) * (num % 10 + 1) + res
        i += 1
        num = num // 10
    return res

print(add1_string(9))
print(add1_string(998))
print(add1_num(9))
print(add1_num(998))
