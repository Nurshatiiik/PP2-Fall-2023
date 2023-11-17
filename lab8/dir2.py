import os
path = r"C:\Users\nurshatserik\OneDrive\text.txt"

if not os.path.exists(path):
    print("Path does not exist!")
else:
    if os.access(path, os.R_OK):
        print("Path is readable.")
    else:
        print("Path is not readable.")
    
    if os.access(path, os.W_OK):
        print("Path is writable.")
    else:
        print("Path is not writable.")
    
    if os.access(path, os.X_OK):
        print("Path is executable.")
    else:
        print("Path is not executable.")