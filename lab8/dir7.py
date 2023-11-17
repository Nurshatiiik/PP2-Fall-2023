with open('text.txt', 'r') as input_file:
    file_contents = input_file.read()

with open('output_file.txt', 'w') as output_file:
    output_file.write(file_contents)