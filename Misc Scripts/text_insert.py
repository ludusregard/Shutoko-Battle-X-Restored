import struct

def endian_swap(value):
    return struct.unpack("<I", struct.pack(">I", value))[0]

def insert_string_in_bin(file_path, new_string, insert_index):
    # Read the file content
    with open(file_path, "rb") as f:
        content = f.read()

    # Extract number of strings
    num_strings = endian_swap(struct.unpack(">I", content[:4])[0])
    
    # Extract pointers
    pointers = [struct.unpack(">I", content[4 + i * 4: 8 + i * 4])[0] for i in range(num_strings)]
    
    # Compute the offset for the new string
    string_start = pointers[insert_index - 1] if insert_index > 1 else 4 + num_strings * 4
    new_string_utf16 = new_string.encode('utf-16le')
    new_string_length = len(new_string_utf16)

    # Create new content with the inserted string
    new_content = content[:string_start] + new_string_utf16 + content[string_start:]
    
    # Update pointers
    new_pointers = pointers[:insert_index - 1] + [string_start] + pointers[insert_index - 1:]
    new_pointers = [endian_swap(p) for p in new_pointers]

    # Create new binary data
    new_num_strings = num_strings + 1
    new_binary = struct.pack(">I", endian_swap(new_num_strings)) + \
                 b''.join(struct.pack(">I", p) for p in new_pointers) + \
                 new_content[4 + num_strings * 4:]
    
    # Write the modified content to a new file with "_ins" suffix
    new_file_path = file_path.replace(".bin", "_ins.bin")
    with open(new_file_path, "wb") as f:
        f.write(new_binary)
    
    print(f"String inserted and file saved as {new_file_path}")

if __name__ == "__main__":
    file_path = input("Enter the .bin file path: ")
    new_string = input("Enter the new string to insert: ")
    insert_index = int(input("Enter the position to insert the new string (1-based index): "))
    
    insert_string_in_bin(file_path, new_string, insert_index)
