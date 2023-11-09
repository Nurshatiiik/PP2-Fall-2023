import re
with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()
def find_str(string):
    print(''.join(x.capitalize() or '_' for x in string.split('_')))
string = input()
find_str(string)