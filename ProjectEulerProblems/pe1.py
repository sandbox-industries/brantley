answer = 0
for num in range(1000):
    if num % 3 == 0 or num % 5 == 0:
        answer += num
print(answer)
print(sum([(lambda x: x if (x % 3 == 0 or x % 5 == 0) else 0)(x) for x in range(1000)]))
