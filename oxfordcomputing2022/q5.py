water = 0

miles = int(input())

complete = 0

for mile in range(miles):
    complete += 1
    water += 30

    if complete == 3:
        water += 10
        complete = 0


print(water)
