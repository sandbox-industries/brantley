from math import sqrt

with open('p042_words.txt', 'r') as file:
    words = file.read().replace('"', '').split(',')


def get_nth_term(num):
    return (1/2) * num * (num + 1)


# print(get_nth_term(10))


# print((sqrt(111 - (sqrt(111) // 1)) % 1) == 0)


def is_triangle_word(word):
    num = sum(list(map(lambda a: ord(a) - 64, word)))

    if get_nth_term(sqrt(num * 2) // 1) == num:
        return True
    else:
        return False


count = 0
for w in words:
    if is_triangle_word(w):
        count += 1
print(count)
#
# print(sum([sqrt((sum(list(map(lambda a: ord(a) - 64, w))) * 2) - sqrt(sum(list(map(lambda a: ord(a) - 64, w))) * 2) // 1) % 1 == 0 for w in open('p042_words.txt', 'r').read().replace('"', '').split(',')]))

# print(sqrt(90 - 9))
# print()
# print(sqrt(90 - 9) % 1)




