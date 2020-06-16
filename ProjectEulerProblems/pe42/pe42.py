from math import sqrt

with open('p042_words.txt', 'r') as file:
    words = file.read().replace('"', '').split(',')


def get_nth_term(num):
    return (1/2) * num * (num + 1)


def is_triangle_word(word):
    num = sum(list(map(lambda a: ord(a) - 64, word)))

    return get_nth_term(sqrt(num * 2) // 1) == num


count = 0
for w in words:
    if is_triangle_word(w):
        count += 1
print(count)

# One line using slightly different logic
print(sum([sqrt((sum(list(map(lambda a: ord(a) - 64, w))) * 2) - sqrt(sum(list(map(lambda a: ord(a) - 64, w))) * 2) // 1) % 1 == 0 for w in open('p042_words.txt', 'r').read().replace('"', '').split(',')]))





