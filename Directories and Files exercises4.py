import os
def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for _ in file)