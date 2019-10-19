hours = [0]*24

for i in range(int(input())):
    a, b = map(int, input().split())
    for j in range(a,b):
        hours[j] = 1

print(sum(hours))
