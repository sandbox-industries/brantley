import math

count = 1
num = 3
while count != 10001:
    prime = True
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            prime = False

