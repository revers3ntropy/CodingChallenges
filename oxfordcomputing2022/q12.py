import collections

string = input()

frequencies = collections.Counter(string)

max_ = 0

for char in frequencies:
    if frequencies[char] > max_:
        max_ = frequencies[char]

most = []

for char in frequencies:
    if frequencies[char] == max_:
        most.append(char)

if len(most) == 1:
    print(most[0])
else:
    most.sort()
    print(' '.join(most))
