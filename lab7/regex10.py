import re
with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()
def find_str(string):
    string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
    print(re.sub('([a-z0-9])([A-Z])', r'\1_\2', string).lower())
string = input()
find_str(string)