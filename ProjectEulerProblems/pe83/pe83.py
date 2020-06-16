import time

with open('p083_matrix.txt', 'r') as file:
    data = file.read()
    data = data.replace('\n', ',')
    data = data.split(',')
    # print(len(data))
    data = [data[x: (x + 80)] for x in range(0, len(data) - 80, 80)]
    print(len(data[79]))
    # data = [data[x:80] for x in range(0, len(data), 80)]
    # print(len(data[3]))

class Node:
    def __init__(self, dig, line_number, idx, up=None, down=None, left=None, right=None):
        self.value = dig
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.path_to_sum = 0
        self.line = line_number
        self.idx = idx
        self.visited = False


start = time.time()

for line_number in range(len(data)):

    data[line_number] = list(map(int, data[line_number]))
    for idx, dig in enumerate(data[line_number]):
        curr_node = Node(dig, line_number, idx)
        data[line_number][idx] = curr_node
        if line_number != 0:
            prev_up = data[line_number - 1][idx]
            data[line_number][idx].up = prev_up

            if line_number < len(data):

                data[line_number - 1][idx].down = data[line_number][idx]


        if idx != 0:
            prev_left = data[line_number][idx - 1]
            data[line_number][idx].left = prev_left

            if idx < len(data[line_number]):
                data[line_number][idx - 1].right = data[line_number][idx]

        # data[line_number][idx] = curr_node


for x in data:
    for y in x:
        print(y.value, end=' ')
    print()


def find_answer(prev_node, curr_node, came_from):
    curr_node.visited = True
    if not prev_node:
        curr_node.path_to_sum = curr_node.value

    elif curr_node.path_to_sum < curr_node.value + prev_node.path_to_sum:

        curr_node.path_to_sum = curr_node.value + prev_node.path_to_sum

    else:
        return

    if curr_node.right is None and curr_node.down is None:
        return

    if curr_node.left and not curr_node.left.visited:
        find_answer(curr_node, curr_node.left, 'right')

    if curr_node.up and not curr_node.up.visited:
        find_answer(curr_node, curr_node.up, 'down')

    if curr_node.right and not curr_node.right.visited:
        find_answer(curr_node, curr_node.right, 'left')

    if curr_node.down and not curr_node.down.visited:
        find_answer(curr_node, curr_node.down, 'up')



find_answer(None, data[0][0], None)
print()
print(data[-1][-1].path_to_sum)

print('up', data[2][2].up.value)
print('down', data[2][2].down.value)
print('left', data[2][2].left.value)
print('right', data[2][2].right.value)





