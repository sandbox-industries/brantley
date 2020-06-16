print((sum([x for x in range(101)])**2) - (sum([(lambda x: x**2)(x) for x in range(101)])))
