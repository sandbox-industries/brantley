import time
number = 1000


def find_triplet(target_number):
    
    for a in range(1, target_number + 1):
        for b in range(a + 1, target_number + 1 - a):

            c = target_number - a - b

            if ((a**2) + (b**2)) == (c**2):
                return a * b * c


start = time.time()

print(find_triplet(number))

print(time.time() - start)
