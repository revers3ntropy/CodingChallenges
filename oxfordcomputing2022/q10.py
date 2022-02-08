n = int(input())

measures = []

for i in range(n):
    measures.append(int(input()))

uphill = 0

for i in range(1, n):
    if measures[i-1] < measures[i]:
        uphill += 100

print(uphill)