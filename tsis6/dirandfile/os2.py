import os
a = input()
print("existance:",os.access(a, os.F_OK))
print("readability", os.access(a, os.R_OK))
print("writability:", os.access(a, os.W_OK))
print("executability:", os.access(a, os.X_OK))