def check(s):
    n = len(s)
    if n < 2:
        return True
    elif n == 2 and s != "ei":
        return True
    for i in range(n-2):
        if s[i+1] == 'e' and s[i+2] == 'i':
            if s[i] == 'c':
                return True
            else:
                return False
        if s[i+1] == 'i' and s[i+2] == 'e':
            if s[i] == 'c':
                return False
            else:
                return True
    return True

print(check("a"))# => true
print(check("zombie"))# => true
print(check("transceiver"))# => true
print(check("veil"))# => false
print(check("icier"))# => false
