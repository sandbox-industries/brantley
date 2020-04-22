from time import time


def fill_in(rows):
    row_idx, col_idx = zero(rows)

    if row_idx == -1:
        return True

    for x in range(1, 10):
        if check(row_idx, col_idx, rows, str(x)):
            rows[row_idx][col_idx] = str(x)

            if fill_in(rows):
                return True

            rows[row_idx][col_idx] = '0'

    return False


def check(row_idx, col_idx, rows, num):
    if num in rows[row_idx]:
        return False

    for row in rows:
        if row[col_idx] == num:
            return False

    for r in range(row_idx // 3 * 3, row_idx // 3 * 3 + 3):
        for c in range(col_idx // 3 * 3, col_idx // 3 * 3 + 3):
            if rows[r][c] == num:
                return False
    return True


def zero(puzzle):
    for row_idx, elm in enumerate(puzzle):
        for col_idx, dig in enumerate(elm):
            if dig == '0':
                return row_idx, col_idx

    return -1, -1


with open('p096.txt', 'r') as file:
    puzzles = file.read().splitlines()

answer = 0

o_start = time()
for x in range(1, len(puzzles), 10):

    puzzle = [list(line) for line in puzzles[x: (x + 9)]]
    fill_in(puzzle)
    answer += int(''.join(puzzle[0][:3]))

print(time() - o_start)
print(answer)
