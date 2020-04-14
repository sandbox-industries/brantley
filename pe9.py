import time

start = time.time()

number = 1000

for a in range(1, number + 1):
    for b in range(a + 1, number + 1 - a):

        c = number - a - b

        if ((a * a) + (b * b)) == (c * c):
            print(a * b * c)

print(time.time() - start)
