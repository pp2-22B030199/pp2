import string
import os
# with open(letter + '.txt', 'w') as wr:
for letter in string.ascii_uppercase:
    with open(letter + '.txt', 'w') as wr:
        wr.write('%s ' %letter)