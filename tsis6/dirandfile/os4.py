import os

file = open('row.txt', 'r')

content = file.read()

cnt = 0
for i in content:
    if i == '\n':
        cnt += 1

print(cnt + 1)