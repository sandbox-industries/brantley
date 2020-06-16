num = 600851475143

max_factor = -1
factor = num
while True:
    no_factors_left = True
    for x in range(3, factor, 2):
        if x == factor:
            continue
        possible_factor = factor / x
        if possible_factor % 1 == 0:
            factor = int(possible_factor)
            max_factor = max(max_factor, x)
            no_factors_left = False
            break

    if no_factors_left:
        max_factor = max(max_factor, factor)
        break
print(max_factor)