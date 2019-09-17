def ap_helper(num, n):
    if num < 10:
        return n
    sum = 0
    while num > 0:
        sum += num%10
        num //= 10
    return ap_helper(sum, n + 1)

def ap(num):
    return ap_helper(num, 0)

print(ap(13))
print(ap(1234))
print(ap(9876))
print(ap(199))
