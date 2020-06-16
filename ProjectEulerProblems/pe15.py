from pprint import pprint


def build_grid(size):
    return [[0 for y in range(size*2)] for x in range(size*2)]


grid = build_grid(5)
for x in grid:
    print(x)
current_position = (0, 0)
# print(grid[len(grid) - 1][len(grid) - 1])
# line, idx = current_position
# print(grid[line][idx])


def find_paths(curr_pos):
    # print(curr_pos)
    line, idx = curr_pos
    grid[line][idx] += 1
    if line == len(grid) - 3 and idx == len(grid) - 1:
        return
    if line == len(grid) - 1 and idx == len(grid) - 3:
        return


    if line % 2 == 0:
        line_add = 1
    else:
        line_add = 2
    if idx % 2 == 0:
        idx_add = 1
    else:
        idx_add = 2

    if line < len(grid) - 1:
        find_paths((line + line_add, idx))
    # if line < len(grid) - 1:
    #     find_paths((line + 1, idx))
    if idx < len(grid) - 1:
        find_paths((line, idx + idx_add))

    # if idx < len(grid) - 1:
    #     find_paths((line, idx + 1))


find_paths((0, 0))
print(len(grid))
# print(grid[len(grid) - 1])

for x in grid:
    print(x)
