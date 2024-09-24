import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Possible save file names
possible_files = ["TXR_DATA_1", "OLD_ITC_TXR_DATA_1", "OLD_SBX_TXR_DATA_1"]
found_files = []

# Check if any of the possible files exist in the script's folder
for file_name in possible_files:
    file_path = os.path.join(script_dir, file_name)
    if os.path.exists(file_path):
        found_files.append(file_path)

# If no valid save file is found, prompt the user for an explicit path
if not found_files:
    user_input = input("No ITC/SBX save file found! Would you like to give an explicit path? [ Y | N ]: ").strip().lower()
    
    if user_input == 'n':
        print("Exiting script.")
        exit()
    elif user_input == 'y':
        # Prompt user for the explicit file path
        save_file_path = input("Please provide the explicit path to the save file: ").strip()
        if not os.path.exists(save_file_path):
            print("Invalid file path. Exiting script.")
            exit()
        found_files.append(save_file_path)
    else:
        print("Invalid input. Exiting script.")
        exit()

# If multiple files are found, prompt the user to select one
if len(found_files) > 1:
    print("Multiple valid save files found:")
    for i, file_path in enumerate(found_files, 1):
        print(f"{i}. {os.path.basename(file_path)}")
    
    # Prompt the user to choose which file to process
    choice = int(input("Select the file to process (by number): ").strip())
    if choice < 1 or choice > len(found_files):
        print("Invalid choice. Exiting script.")
        exit()
    
    save_file_path = found_files[choice - 1]
else:
    # Only one file found
    save_file_path = found_files[0]

# Determine file size and auto-detect the game type
file_size = os.path.getsize(save_file_path)

if file_size == 129400:
    game_type = 'itc'
elif file_size == 129200:
    game_type = 'sbx'
else:
    print("Unrecognized file size. Exiting script.")
    exit()

# Define the renaming and file sizes for ITC and SBX conversions
if game_type == 'itc':
    old_file_name = "OLD_ITC_TXR_DATA_1"
    new_file_size = 129200  # 129,200 bytes for SBX
    car_chunk_size = 1968  # 1968 bytes per chunk for ITC
    car_chunk_skip = 1578
    insert_bytes = b'\x01\x03\x01\x01\x01\x01\x01\x01\x01'
elif game_type == 'sbx':
    old_file_name = "OLD_SBX_TXR_DATA_1"
    new_file_size = 129400  # 129,400 bytes for ITC
    car_chunk_size = 1964  # 1964 bytes per chunk for SBX
    car_chunk_skip = 1574
    insert_bytes = b'\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00'

output_file_name = "TXR_DATA_1"
output_file_path = os.path.join(script_dir, output_file_name)

# Rename the input file to OLD_ITC_TXR_DATA_1 or OLD_SBX_TXR_DATA_1
os.rename(save_file_path, os.path.join(script_dir, old_file_name))

# Create the new file with all bytes set to 0x00
with open(output_file_path, 'wb') as output_file:
    output_file.write(b'\x00' * new_file_size)

# Handle the first 6336 bytes (Header)
header_size = 6336

# Open the renamed input file in binary mode
with open(os.path.join(script_dir, old_file_name), 'rb') as input_file:
    # Read the first 6336 bytes (Header)
    header_data = input_file.read(header_size)

# Write the header data to the new file
with open(output_file_path, 'r+b') as output_file:
    output_file.seek(0)
    output_file.write(header_data)

# Handle the Garage Info section (up to 50 car chunks)
max_cars = 50

with open(os.path.join(script_dir, old_file_name), 'rb') as input_file, open(output_file_path, 'r+b') as output_file:
    # Seek to the first car chunk (immediately after the header)
    input_file.seek(header_size)
    output_file.seek(header_size)
    
    for car_index in range(max_cars):
        car_chunk = input_file.read(car_chunk_size)
        
        # Copy first 1565 bytes of the chunk
        output_file.write(car_chunk[:1565])
        
        # Write the insertion bytes based on game type
        output_file.write(insert_bytes)
        
        # Copy the remaining bytes from the chunk, skipping over the defined region
        output_file.write(car_chunk[car_chunk_skip:])

# Handle the last 24672 bytes (Unlocked Cars & Rivals Defeated)
chunk_size = 24672

# Reopen the input file to seek and read the last chunk
with open(os.path.join(script_dir, old_file_name), 'rb') as input_file:
    # Seek to the start of the "Unlocked Cars & Rivals Defeated" section in the input file
    input_file.seek(-chunk_size, os.SEEK_END)
    
    # Read the last 24672 bytes
    last_chunk = input_file.read(chunk_size)

# Write these bytes to the end of the new file
with open(output_file_path, 'r+b') as output_file:
    output_file.seek(-chunk_size, os.SEEK_END)
    output_file.write(last_chunk)

print(f"New file '{output_file_name}' created with size {new_file_size} bytes.")
print(f"Renamed input file to '{old_file_name}' and copied the first {header_size} bytes (Header), the 'Garage Info' car chunks, and the last {chunk_size} bytes (Unlocked Cars & Rivals Defeated) from the input save file.")
