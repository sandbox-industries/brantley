import numpy as np
from timeit import default_timer as timer


def poow(a, b, c):
    for i in range(a.size):
         c[i] = a[i] ** b[i]


def main():
    vec_size = 100000000

    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)

    start = timer()
    poow(a, b, c)
    duration = timer() - start

    print(duration)


if __name__ == '__main__':
    main()

    (2m) ^ 2 + (m ^ 2 - 1) ^ 2 = (m ^ 2 + 1) ^ 2