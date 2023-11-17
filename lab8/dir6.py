import string
alphabet = string.ascii_uppercase
file_names = [f"{letter}.txt" for letter in alphabet]
for file_name in file_names:
    with open(file_name, "w") as f:
        pass