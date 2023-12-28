import os

# Get the current working directory
current_directory = os.getcwd()

# Get all files and directories in the current directory
for filename in os.listdir(current_directory):
    # Construct full file path
    filepath = os.path.join(current_directory, filename)
    # Check if this is a directory
    if os.path.isdir(filepath):
        print(f'Directory: {filepath}')
    else:
        print(f'File: {filepath}')

