import re
txt = input()
# for i in txt:
s = re.sub("[,.]" , ":", txt)

print(s)


