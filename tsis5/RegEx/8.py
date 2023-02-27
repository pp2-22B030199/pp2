#8
# import re
# s = input()
# x = re.split('[A-Z]', s)
# print(x)
#9
# import re
# x = input()
# s = re.sub(r"( )([A-Z])",r"\1 \2",x)
# print(s)
#10
import re
x = input()
s = re.sub(r"(\w)([A-Z])",r"\1_\2",x)
y = s.lower()
print(y)