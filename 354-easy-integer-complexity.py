def small(a):
    root = int(a**0.5)
    min_sum = 10000000000
    for i in range(1, root+1):
        if i*(a//i) == a and i + a//i < min_sum:
            min_sum = i + a//i

    return min_sum

print(small(12345))
print(small(12))
print(small(456))
print(small(4567))
print(small(345678))
