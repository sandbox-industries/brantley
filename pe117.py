length = 5

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


answer = [0 for x in range(51)]
answer[0] = 1

# Stolen from egnor.
for i in range(len(answer)):
    for x in range(1, 5):
        if i - x >= 0:
            answer[i] += answer[i - x]
print(answer[50])


print(fcomb(0, 0))
