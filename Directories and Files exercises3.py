import os
def path_info(path):
    if os.path.exists(path):
        return os.path.basename(path), os.path.dirname(path)
    return "Path does not exist."