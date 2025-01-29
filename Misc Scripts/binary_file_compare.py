import os

def compare_files(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        while True:
            chunk1 = f1.read(4096)
            chunk2 = f2.read(4096)

            # Check if chunks are identical
            if chunk1 != chunk2:
                # Check if there's a single extra null byte at the end of file
                if chunk1 == chunk2 + b'\x00' or chunk2 == chunk1 + b'\x00':
                    continue
                return False
            if not chunk1:  # End of both files
                break
    return True

def compare_folders(folder1, folder2):
    files1 = set(os.listdir(folder1))
    files2 = set(os.listdir(folder2))

    common_files = files1.intersection(files2)
    
    for file in common_files:
        file1 = os.path.join(folder1, file)
        file2 = os.path.join(folder2, file)

        if os.path.isfile(file1) and os.path.isfile(file2):
            if compare_files(file1, file2):
                print(f"{file}: Same")
            else:
                print(f"{file}: Different")
        else:
            print(f"{file}: Not a file in one or both folders")

def main():
    folder1 = input("Enter the path of the first folder: ")
    folder2 = input("Enter the path of the second folder: ")

    if not os.path.exists(folder1) or not os.path.exists(folder2):
        print("One or both of the folder paths are invalid. Please check the paths and try again.")
        return

    compare_folders(folder1, folder2)

# Run the script
main()
