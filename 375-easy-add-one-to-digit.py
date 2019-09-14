def add1_string(num):
    return ''.join(['' + (str(int(i) + 1)) for i in str(num)])

print(add1_string(9))
print(add1_string(998))
