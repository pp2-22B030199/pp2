import os

with os.scandir('dir/') as enteries:
    print("Files and Directories:")
    for entry in enteries:
        print(entry.name)