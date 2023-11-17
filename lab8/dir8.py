import os
path = r"C:\Users\nurshatserik\OneDrive\text.txt"

if os.path.exists(path):
    os.remove(path)
else:
    print(f"Path {path} does not exist")