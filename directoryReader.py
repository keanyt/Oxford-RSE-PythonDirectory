import os
import sys


def print_directory_tree(path, level=1):

    # Get the list of files and directories in the current path
    files_and_dirs = os.listdir(path)

    # Sort the list to have files first and folders second
    files_and_dirs.sort(key=lambda x: os.path.isdir(os.path.join(path, x)))

    # Loop through folders
    for item in files_and_dirs:

        # Build the full path of the item
        item_path = os.path.join(path, item)

        # Print the item with 4 char indentation and add a / if it's a folder
        print("    " * level + item + ("/" if os.path.isdir(item_path) else ""))
        # If tabs are desired
        #print("\t" * level + item + ("/" if os.path.isdir(item_path) else ""))

        # If the item is a folder, recursively print contents
        if os.path.isdir(item_path):
            print_directory_tree(item_path, level + 1)


# Check if input is a valid file path (assuming minimum possible is a disk ref. like C:)
if len(sys.argv) < 2:
    print("Please provide a valid file path as an argument.")
    sys.exit(1)

# Get the file path from the command line argument
file_path = sys.argv[1]

# Check if the provided file path exists
if not os.path.exists(file_path):
    print(f"The path '{file_path}' does not exist.")
    sys.exit(1)

# Print the directory tree
baseline = os.path.basename(file_path) + "/"
print(baseline)
print_directory_tree(file_path)