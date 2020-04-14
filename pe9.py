import time

start = time.time()

number = 1000

for a in range(1, number + 1):
    for b in range(a + 1, number + 1 - a):

        c = number - a - b

        if ((a**2) + (b**2)) == (c**2):
            print(a * b * c)

print(time.time() - start)
