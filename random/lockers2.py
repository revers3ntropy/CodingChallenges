import math
n = 1000
print([(1 if int(math.sqrt(i) + 0.5) ** 2 == i else 0) for i in range(n)].count(1)-1)
