import itertools as it

def fit1(big_x, big_y, small_x, small_y):
    return (big_x//small_x)*(big_y//small_y)

def fit2(big_x, big_y, small_x, small_y):
    same = fit1(big_x, big_y, small_x, small_y)
    flipped = fit1(big_x, big_y, small_y, small_x)

    max_crates = max(same, flipped)
    return max_crates;

def fit3(a, b, c, x, y, z):
    big = list([a, b, c])
    small = it.permutations([x, y, z])
    res = 0
    for j in small:
        k = (big[0]//j[0])*(big[1]//j[1])*(big[2]//j[2])
        res = max(res, k)
    return res

def fitn(large_crate, small_crate):
    small = it.permutations(small_crate)
    l = len(large_crate)
    res = 0
    for j in small:
        product = 1
        for k in range(l):
            product = product*(large_crate[k]//j[k])
        res = max(res, product)
    return res


print("fit1")
print(fit1(25, 18, 6, 5))
print(fit1(10, 10, 1, 1))
print(fit1(12, 34, 5, 6))
print(fit1(12345, 678910, 1112, 1314))
print(fit1(5, 100, 6, 1))

print("\nfit2")
print(fit2(25, 18, 6, 5))
print(fit2(12, 34, 5, 6))
print(fit2(12345, 678910, 1112, 1314))
print(fit2(5, 5, 3, 2))
print(fit2(5, 100, 6, 1))
print(fit2(5, 5, 6, 1))

print("\nfit3")
print(fit3(10, 10, 10, 1, 1, 1))
print(fit3(12, 34, 56, 7, 8, 9))
print(fit3(123, 456, 789, 10, 11, 12))
print(fit3(1234567, 89101112, 13141516, 171819, 202122, 232425))

print("\nfit20")
print(fitn([3, 4], [1, 2]))
print(fitn([123, 456, 789], [10, 11, 12]))
print(fitn([123, 456, 789, 1011, 1213, 1415], [16, 17, 18, 19, 20, 21]))
print(fitn([180598, 125683, 146932, 158296, 171997, 204683, 193694, 216231, 177673, 169317, 216456, 220003, 165939, 205613, 152779, 177216, 128838, 126894, 210076, 148407], [1984, 2122, 1760, 2059, 1278, 2017, 1443, 2223, 2169, 1502, 1274, 1740, 1740, 1768, 1295, 1916, 2249, 2036, 1886, 2010]))
# 4281855455197643306306491981973422080000
