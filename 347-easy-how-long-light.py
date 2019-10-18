hours = [0]*24

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a,b):
        hours[j] = 1

print(sum(hours))
