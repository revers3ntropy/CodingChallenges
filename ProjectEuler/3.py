n = 600851475143

i = 1
while n != 1:
    i += 1
    while 1:
        if n % i == 0:
            n = n / i
        else:
            break

print(i)
