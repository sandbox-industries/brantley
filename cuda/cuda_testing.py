import numpy as np
from timeit import default_timer as timer
from numba import vectorize, guvectorize, jit


@vectorize(['float32(float32, float32)'], target='cuda')
def pow(a, b):
    return a ** b


@vectorize(target='parallel')
def g(x, y):
    res = []
    for i in range(x.shape[0]):
        res.append(x[i] + y[i])
    return res

def main():
    vec_size = 100000000

    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    # c = np.zeros(vec_size, dtype=np.float32)
    c = list()
    start = timer()
    c = g(a, b)
    duration = timer() - start

    print(duration)


if __name__ == '__main__':
    main()