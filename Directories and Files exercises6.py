import os
def generate_alphabet_files():
    for char in range(65, 91):  # ASCII values for A-Z
        with open(f"{chr(char)}.txt", 'w') as file:
            file.write(f"This is file {chr(char)}.txt\n")