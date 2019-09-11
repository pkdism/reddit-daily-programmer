def fit1(big_x, big_y, small_x, small_y):
    return (big_x//small_x)*(big_y//small_y)

def fit2(big_x, big_y, small_x, small_y):
    same = fit1(big_x, big_y, small_x, small_y)
    flipped = fit1(big_x, big_y, small_y, small_x)

    max_crates = max(same, flipped)
    return max_crates;

def fit3(a, b, c, x, y, z):
    p1 = (a//x)*(b//y)*(c//z)
    p2 = (a//x)*(b//z)*(c//y)
    p3 = (a//y)*(b//z)*(c//x)
    p4 = (a//y)*(b//x)*(c//z)
    p5 = (a//z)*(b//x)*(c//y)
    p6 = (a//z)*(b//y)*(c//x)

    return max(p1, p2, p3, p4, p5, p6)

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
