import os

def remove_data_before_byte_string(input_file, byte_string):
    # Open the input file in binary read mode
    with open(input_file, 'rb') as f:
        # Read the entire content of the file
        data = f.read()

    # Find the index of the byte string
    index = data.find(byte_string)

    # If the byte string is found, write the data from that point to a new file with .xpr extension
    if index != -1:
        new_file_path = input_file.rsplit('.', 1)[0] + '.xpr'
        with open(new_file_path, 'wb') as f:
            f.write(data[index:])
        print(f"Data before {byte_string} removed and saved as {new_file_path}.")
    else:
        print(f"Byte string {byte_string} not found in {input_file}.")

def process_files_recursively(folder_path, byte_string):
    # Walk through all directories and files in the given folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Skip Python files
            if file.endswith('.py'):
                continue

            file_path = os.path.join(root, file)
            try:
                # Process each file
                remove_data_before_byte_string(file_path, byte_string)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

# Usage
folder_path = os.path.dirname(os.path.abspath(__file__))
byte_string = b'\x58\x50\x52\x32'  # Byte string corresponding to "XPR2"

process_files_recursively(folder_path, byte_string)
