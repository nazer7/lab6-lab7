import os

def list_directories_and_files(path):
    if not os.path.exists(path):
        return "Path does not exist."
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return directories, files