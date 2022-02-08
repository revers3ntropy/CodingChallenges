n = int(input())

nums = ''

frequencies = [0 for _ in range(10)]


for i in range(n):
    nums += input()

for digit in nums:
    frequencies[int(digit)] += 1

max_val = 0
max_digit = 0
for j in range(10):
    if frequencies[j] > max_val:
        max_digit = j
        max_val = frequencies[j]

print(max_digit)
