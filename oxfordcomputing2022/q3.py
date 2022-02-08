import math

cash = int(input())

towns_profit = map(int, input().split(' '))

for profit in towns_profit:
    cost = math.floor(cash/2)
    if profit > cost:
        cash -= cost
        cash += profit

print(cash)
