def derangement(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    return (n-1)*(derangement(n-1) + derangement(n-2))

print(derangement(2))
print(derangement(3))
print(derangement(5))
print(derangement(6))
print(derangement(9))
print(derangement(14))
