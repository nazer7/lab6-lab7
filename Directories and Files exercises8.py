import os
def delete_file(file_path):
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        return f"File '{file_path}' deleted."
    return "File does not exist or cannot be deleted."
