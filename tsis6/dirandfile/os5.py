import os

mylist = input().split()
with open('input.txt', 'w') as wr:
    for i in mylist:
        wr.write('%s ' %i)