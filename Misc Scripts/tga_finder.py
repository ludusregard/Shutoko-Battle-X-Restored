import os

def check_footer_and_rename(input_file, footer):
    # Open the input file in binary read mode
    with open(input_file, 'rb') as f:
        # Seek to the end of the file minus the length of the footer
        f.seek(-len(footer), os.SEEK_END)
        # Read the final bytes of the file
        file_footer = f.read(len(footer))

    # If the footer matches, rename the file to have a .tga extension
    if file_footer == footer:
        new_file_name = os.path.splitext(input_file)[0] + '.tga'
        os.rename(input_file, new_file_name)
        print(f"Renamed: {input_file} -> {new_file_name}")
    else:
        print(f"No matching footer in: {input_file}")

def process_files_recursively(folder_path, footer):
    # Walk through all directories and files in the given folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Process each file
                check_footer_and_rename(file_path, footer)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

# Get the folder where the Python script is located
folder_path = os.path.dirname(os.path.abspath(__file__))

# Footer corresponding to "TRUEVISION-XFILE.\0"
footer = b'\x54\x52\x55\x45\x56\x49\x53\x49\x4F\x4E\x2D\x58\x46\x49\x4C\x45\x2E\x00'

# Process files recursively in the script's directory
process_files_recursively(folder_path, footer)
