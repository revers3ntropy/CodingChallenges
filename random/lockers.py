n = 10000
lockers = [False] * n

for student in range(n):
    for lockerN in range(n):
        if lockerN % (student+1):
            lockers[lockerN] = not lockers[lockerN]
            
print(lockers.count(True))
