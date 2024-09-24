import os

def unlock_cars(file_path, offset):
    with open(file_path, 'rb+') as f:

        # Create a backup before making any changes
        backup_file_path = f"{file_path}_unmodified"
        with open(backup_file_path, 'wb') as backup_file:
            f.seek(0)
            backup_file.write(f.read())
        
        # Begin changes
        f.seek(offset)        
        modified = False

        # 1st byte check and replace
        first_byte = f.read(1)
        if first_byte == b'\x6B':
            f.seek(-1, os.SEEK_CUR)
            f.write(b'\x7F')
            print("AE86 Trueno and Levin unlocked")
            modified = True
        # If player has unlocked Devil Z already
        elif first_byte == b'\xEB':
            f.seek(-1, os.SEEK_CUR)
            f.write(b'\xFF')
            print("AE86 Trueno and Levin unlocked")
            modified = True

        # 2nd byte, always replace with FF
        second_byte = f.read(1)
        if second_byte != b'\xFF':
            f.seek(-1, os.SEEK_CUR)
            f.write(b'\xFF')
            print("S30 Fairlady Z unlocked")
            modified = True

        # 3rd byte check and replace
        third_byte = f.read(1)
        if third_byte == b'\xF3':
            f.seek(-1, os.SEEK_CUR)
            f.write(b'\xFB')
            print("Mitsubishi Eclipse unlocked")
            modified = True
        # If player has unlocked Skull Bullet already
        elif third_byte == b'\xF7':
            f.seek(-1, os.SEEK_CUR)
            f.write(b'\xFF')
            print("Mitsubishi Eclipse unlocked")
            modified = True

        # Check if change happened
        if modified:
            print("Cut cars unlocked, have a Genki day!")
        else:
            print("No cars unlocked.")
            # Delete the backup if no changes were made
            if os.path.exists(backup_file_path):
                os.remove(backup_file_path)
                print("Backup file deleted as no changes were made.")

def main():
    # Ask the user for the file type
    save_type = input('Type "en" for Import Tuner Challenge save file or type "jp" for Shutoko Battle X save: ').strip().lower()
    
    # Determine the offset based on the save type
    if save_type == "en":
        offset = 0x19925  # Offset for Import Tuner Challenge
    elif save_type == "jp":
        offset = 0x1985D  # Offset for Shutoko Battle X
    else:
        print("Invalid input. Please type 'en' or 'jp'.")
        return  # Exit if the input is invalid
        
    # Default ITC/SBX save file name
    file_path = os.path.join(os.getcwd(), "TXR_DATA_1")

    # Check if the save file exists in the current directory
    if not os.path.exists(file_path):
        # Ask the user to provide the correct file name if not found
        file_path = input("No Shutoko Battle X save data found, please input the save file name: ")

    # Run the unlock function
    unlock_cars(file_path, offset)

# Start the script
if __name__ == "__main__":
    main()
