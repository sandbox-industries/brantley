import time
start = time.time()

def is_palindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    return False


max_palindrome = -1
pal_i = 0
for x in range(1000, 99, -1):
    if x < pal_i:
        break
    for i in range(999, 99, -1):
        if is_palindrome(x * i):
            pal_i = i
            max_palindrome = max(max_palindrome, (x * i))
print(time.time() - start)
print(max_palindrome)
