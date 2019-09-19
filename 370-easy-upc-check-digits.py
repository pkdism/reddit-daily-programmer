def upc(num):
    num = str(num)
    l = len(num)
    num = '0'*(11-l) + num
    odd_sum, even_sum = 0, 0
    for i in range(11):
        if i % 2 == 0:
            odd_sum += int(num[i])
        else:
            even_sum += int(num[i])
    res = (odd_sum * 3 + even_sum) % 10
    print(res)
    if res == 0:
        return 0
    else:
        return (10 - res)

print(upc(4210000526))
print(upc(3600029145))
print(upc(12345678910))
print(upc(1234567))
