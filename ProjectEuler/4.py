largest = 0
for i in range(100, 1001):
    for j in range(100, 1001):
        prod = i*j
        if str(prod)[::-1] == str(prod) and prod > largest:
            largest = prod
print(largest)
