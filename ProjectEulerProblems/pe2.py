# Checking one at a time
prev_num = 1
curr_num = 2
answer = 0
while curr_num < 4000000:
    if curr_num % 2 == 0:
        answer += curr_num
    curr_num += prev_num
    prev_num = curr_num - prev_num
print(answer)

# Checking two at a time
total_sum = 0
first_num = 1
second_num = 2
while second_num < 4000001:
    if first_num % 2 == 0:
        total_sum += first_num
    if second_num % 2 == 0:
        total_sum += second_num
    first_num += second_num
    second_num += first_num
print(total_sum)


