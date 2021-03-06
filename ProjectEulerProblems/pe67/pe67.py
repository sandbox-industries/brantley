import time

with open('p067_triangle.txt', 'r') as file:
    triangle_data = file.readlines()


class Node:
    def __init__(self, value, left_p, right_p):
        self.value = value
        self.left_parent = left_p
        self.right_parent = right_p
        self.path_to_sum = value


def find_answer(prev_node, curr_node):
    # Passes when the curr_node is the first node
    if prev_node is not None:
        if curr_node.path_to_sum < curr_node.value + prev_node.path_to_sum:
            curr_node.path_to_sum = curr_node.value + prev_node.path_to_sum

        else:
            return

    if curr_node.right_parent:
        find_answer(curr_node, curr_node.right_parent)

    if curr_node.left_parent:
        find_answer(curr_node, curr_node.left_parent)


start = time.time()

# Creating the tree
for line_number in range(len(triangle_data)):

    triangle_data[line_number] = list(map(int, triangle_data[line_number].split()))

    for idx, dig in enumerate(triangle_data[line_number]):

        right_parent = None
        left_parent = None

        # Node not first in the list. Can have left parent
        if idx != 0:
            left_parent = triangle_data[line_number - 1][idx - 1]

        # Node not last in the list. Can have right parent
        if idx != len(triangle_data[line_number]) - 1:
            right_parent = triangle_data[line_number - 1][idx]

        # Creating node object and inserting it in the data.
        triangle_data[line_number][idx] = Node(dig, left_parent, right_parent)


# Loop through the last line in triangle data and run the find_answer recursive function on each node
for n in triangle_data[-1]:
    print(n)
    find_answer(None, n)

print(time.time() - start)

# Answer
print(triangle_data[0][0].path_to_sum)


