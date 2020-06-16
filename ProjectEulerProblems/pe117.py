length = 20


# fails after a length of 20
def fcomb(prev_tiles, num_tiles):
    answer = 0
    curr_tiles = prev_tiles + num_tiles
    if curr_tiles == length:
        return 1
    if curr_tiles > length:
        return 0

    for x in range(1, 5):
        answer += fcomb(curr_tiles, x)
    return answer


# answer = [0 for x in range(51)]
# answer[0] = 1
#
# # Stolen from egnor.
# for i in range(len(answer)):
#     for x in range(1, 5):
#         if i - x >= 0:
#             answer[i] += answer[i - x]
# print(answer[50])

# print(fcomb(0, 0))

# test = ['a', 'c', 'c', 'c', 'a']
# print(len(set(test)))
# print(set(test))
# print([test.count(value) for value in set(test)])
# print(test[4])






test = ['7777D', '6S', '5D', '3S', '4C']

# test.sort(key=lambda x: int(x.strip(''.join(list(map(chr, range(65, 91)))))))
print(max(1, 1))
# values = [int(x.strip('SHDC')) for x in test]
# print(values == list(range(min(values), max(values) + 1)))


