from numba import njit

i: int = 3
# 2 - 4
sum_ = -2


@njit
def is_prime(n: int):

    for i in range(2, round(n/2)):
        if n % i == 0:
            return False

    return True


while 1:
    if is_prime(i):
        print(i)
        sum_ += i

    i += 1

    if i >= 2000000:
        break

print(sum_)
