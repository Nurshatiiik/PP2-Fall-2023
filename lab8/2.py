def cnt_up_lwr(s):
    upCnt = 0
    lwrCnt = 0
    for char in s:
        if char.isupper():
            upCnt += 1
        elif char.islower():
            lwrCnt += 1

    print("Uppercase:", upCnt)
    print("Lowercase:", lwrCnt)

input_string = input()

cnt_up_lwr(input_string)
