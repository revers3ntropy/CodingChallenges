n = int(input())

necklaces = []

for i in range(n):
    i_ = input().split(' ')
    necklaces.append([int(i_[0]), int(i_[1])])

d = 0
l = 0

while len(necklaces):
    max_r = 0
    max_idx_r = 0
    for [i, [r, s]] in enumerate(necklaces):
        if r > max_r:
            max_r = r
            max_idx_r = i

    necklaces.pop(max_idx_r)

    max_s = 0
    max_idx_s = 0
    for [i, [r, s]] in enumerate(necklaces):
        if s > max_s:
            max_s = s
            max_idx_s = i

    necklaces.pop(max_idx_s)
    l += max_s

print(l)
