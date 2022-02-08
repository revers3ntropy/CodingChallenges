a = 0
b = 0

for _ in range(4):
    [team, time, hits] = input().split(' ')
    if team == 'A':
        a += int(time) - int(hits) * 3
    else:
        b += int(time) - int(hits) * 3

if a == b:
    print('draw')
if a > b:
    print('B')
else:
    print('A')
