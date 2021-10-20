# give it a minute...
i = 2520
while 1:
    i += 1

    valid = True

    for j in range(1, 21):
        if i % j != 0:
            valid = False
            break

    if valid:
        print(i)
        break
