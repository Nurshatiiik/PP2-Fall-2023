import os
path = r"C:\Users\nurshatserik\OneDrive"
directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

print("List of directories in", path)
for directory in directories:
    print(directory)

path = r"C:\Users\nurshatserik\OneDrive"

files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

print("List of files in", path)
for file in files:
    print(file)

path = r"C:\Users\nurshatserik\OneDrive"

directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

print("List of directories and files in", path)
print("Directories:")
for directory in directories:
    print(directory)
print("Files:")
for file in files:
    print(file)