def num_counter(path):
    line_count=0
    with open(path, 'r') as file:
        for line in file:
            line_count += 1
    print(line_count)
path = "text.txt"
num_counter(path)