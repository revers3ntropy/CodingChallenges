
sum = 0

def fib(n, n_1):
    global sum
    old_n = n
    n = n + n_1

    if n > 4000000:
        return

    if n % 2 == 0:
        sum += n
    fib(n, old_n)


fib(1, 1)

print(sum)
