import os
def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write('\n'.join(data))