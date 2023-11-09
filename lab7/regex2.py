import re
with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()
def find_str(string):
     pattern = re.search(r'ab{2}|b{3}', string)
     if pattern:
         print(True)
     else:
         print(False)
string = input()
find_str(string)
