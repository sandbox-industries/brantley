import re
import time
import requests

url = 'https://projecteuler.net/problem=8'
resp = requests.get(url)
resp = resp.content.decode()
resp = resp.replace('<br />', '').replace('\n', '')

num = re.findall('\d{1000}', resp)[0]

start = time.time()
greatest_product = -1

for x in range(len(num)):
    digits = num[x: x + 13]
    if '0' in digits:
        continue
    current_product = 1
    for d in digits:
        current_product *= int(d)
    if current_product > greatest_product:
        greatest_product = current_product

print(greatest_product)  # answer

print(time.time() - start)

