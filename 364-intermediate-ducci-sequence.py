def ducci_util(inp, seqs, count, n):
    if set(inp) == {0} or inp in seqs:
        return count
    seqs.append(inp)
    new = [abs(inp[(i+1)%n] - inp[i%n]) for i in range(n)]
    return ducci_util(new, seqs, count + 1, n)

def ducci(start):
    seqs = []
    return ducci_util(start, seqs, 1, len(start))

print(ducci((1, 5, 7, 9, 9)))
print(ducci((1, 2, 1, 2, 1, 0)))
print(ducci((10, 12, 41, 62, 31, 50)))
print(ducci((10, 12, 41, 62, 31)))
