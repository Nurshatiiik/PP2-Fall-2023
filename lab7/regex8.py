import re
with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()
def find_str(string):
    string = re.split("[A-Z]", string)
    print(string)
string = input()
find_str(string)