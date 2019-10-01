def insert(s):
    l = len(s)
    if l == 0:
        return [1]
    elif l == 1:
        return [1, 1, 0]
    res = []
    for i in range(l):
        res.append(s[i])
        if i != (l-1):
            res.append(1)
            res.append(0)
    return res

res = []
for i in range(8):
    print(i+1)
    res = insert(res)
    print(res)
