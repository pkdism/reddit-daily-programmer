s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def base62(num):
    base = 62
    res = ''
    while(num > 0):
        res += s[num % base]
        num //= base
    return ''.join(res)

print(base62(15674))
print(base62(7026425611433322325))
print(base62(187621))
print(base62(237860461))
print(base62(2187521))
print(base62(18752))
