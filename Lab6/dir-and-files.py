#Problem 1
import os
path = "/path/to/directory"
dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
print(dirs, files, os.listdir(path))


print(" ")
#Problem 2
import os
path = "/path/to/directory"
print(os.access(path, os.F_OK))
print(os.access(path, os.R_OK))
print(os.access(path, os.W_OK))
print(os.access(path, os.X_OK))


print(" ")
#Problem 3
import os
path = "/path/to/file.txt"
if os.path.exists(path):
    print(os.path.basename(path))
    print(os.path.dirname(path))


print(" ")
#Problem 4
file = "file.txt"
with open(file, "r") as f:
    lines = sum(1 for line in f)
print(lines)


print(" ")
#Problem 5
data = ['apple', 'banana', 'cherry']
with open("output.txt", "w") as f:
    for item in data:
        f.write(item + "\n")


print(" ")
#Problem 6
import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}.txt")


print(" ")
#Problem 7
src = "source.txt"
dest = "destination.txt"
with open(src, "r") as s, open(dest, "w") as d:
    d.write(s.read())


print(" ")
#Problem 8
import os
path = "file.txt"
if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
