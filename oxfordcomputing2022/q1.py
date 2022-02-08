import math

n = int(input())

if n > 200:
    print(math.floor(n - n * 0.2))
elif n > 100:
    print(math.floor(n - n * 0.15))
elif n > 50:
    print(math.floor(n - n * 0.1))
else:
    print(math.floor(n))
