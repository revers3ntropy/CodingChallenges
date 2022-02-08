n = int(input())  # the number of error digits to look for in the error codes
A = input().split(' ')  # line of n digits separated by a space (the error digits)
m = int(input())  # the number of error codes

error_codes = []

for i in range(m):
    error_codes.append(input())

errors = 0

for err in error_codes:
    if err[0] in A:
        errors += 1

print(errors)

