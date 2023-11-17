my_list = ['apple', 'banana', 'orange', 'grape']

with open('output_file.txt', 'w') as file:
    for item in my_list:
        file.write("%s\n" % item)