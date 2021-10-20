from numba import njit
# oh my god numba works

i: int = 3
nth_prime: int = 0


@njit
def is_prime(n: int):

    for i in range(2, round(n/2)):
        if n % i == 0:
            return False

    return True


while 1:
    if is_prime(i):
        nth_prime += 1

        if nth_prime == 10001:
            print(i)
            break

    i += 1
