print(sum((sum((num - 64) * (idx + 1) for num in list(map(ord, x)))) for idx, x in enumerate(sorted(open('p022_names.txt', 'r').read().replace('"', '').split(',')))))


with open('p022_names.txt', 'r') as file:
    names = file.read()
    names = names.replace('"', '').split(',')


def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1


merge_sort(names)
print(names)
