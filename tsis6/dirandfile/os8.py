import os
if os.access('dir', os.F_OK):
    print("existance:",True)
os.remove('dir/file.py')