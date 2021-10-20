for a in range(2, 998):
    for b in range(a, 998):
        for c in range(b, 998):
            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    print(a*b*c)
                    exit()
