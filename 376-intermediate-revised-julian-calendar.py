def leaps(start, end):
    ly = 0
    for i in range(start, end, 1):
        flag = False
        if i % 4 == 0:
            flag = True
        if i % 100 == 0:
            flag = False
        if i % 900 in [200, 600]:
            flag = True
        if flag:
            ly += 1
    return ly

print(leaps(2016, 2017))
print(leaps(2019, 2020))
print(leaps(1900, 1901))
print(leaps(2000, 2001))
print(leaps(2800, 2801))
print(leaps(123456, 123456))
print(leaps(1234, 5678))
print(leaps(123456, 7891011))
