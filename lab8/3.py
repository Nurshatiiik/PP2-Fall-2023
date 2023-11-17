def palindrome(string):
    if string == ''.join(reversed(string)):
        return True
    else: return False

s = input()
if palindrome(s):
    print("Yes")
else:
    print("No")