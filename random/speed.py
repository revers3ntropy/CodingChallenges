import time

start = time.time()

def do(n):
    n += 1
    return n

for i in range(1000000):
    do(i);

print(time.time() - start)
