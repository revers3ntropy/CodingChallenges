square_sum = 0
sum_squared = 0

for i in range(1, 101):
    square_sum += i**2
    sum_squared += i

sum_squared **= 2

print(sum_squared - square_sum)
