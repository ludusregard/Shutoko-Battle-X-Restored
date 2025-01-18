import os
import shutil
import subprocess

def clean_temp_folder():
    for item in os.listdir("temp"):
        if item not in ["UnBundler.exe", "Bundler.exe"]:
            item_path = os.path.join("temp", item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)

def dump_xpr():
    # Scan for .xpr files in old_in
    old_in = "old_in"
    xpr_files = [f for f in os.listdir(old_in) if f.endswith(".xpr")]

    if not xpr_files:
        print("No .xpr files found in 'old_in' folder.")
        return

    if len(xpr_files) == 1:
        xpr_file = xpr_files[0]
    else:
        print("Found the following .xpr files:")
        for i, f in enumerate(xpr_files):
            print(f"[{i + 1}] {f}")
        choice = int(input("Type the number of the .xpr file you want to dump: ")) - 1
        xpr_file = xpr_files[choice]

    xpr_name = os.path.splitext(xpr_file)[0]
    xpr_path = os.path.join(old_in, xpr_file)

    # Copy the selected XPR file to temp folder
    shutil.copy(xpr_path, "temp")

    # Create a new folder in old_out with the XPR name
    old_out_folder = os.path.join("old_out", xpr_name)
    os.makedirs(old_out_folder, exist_ok=True)

    # Run UnBundler.exe with the chosen XPR file
    subprocess.run(["temp\\UnBundler.exe", xpr_file], cwd="temp")

    # Rename the .rdf file
    rdf_file = os.path.join("temp", f"{xpr_file}.rdf")
    if os.path.exists(rdf_file):
        new_rdf_file = os.path.join("temp", f"{xpr_name}.rdf")
        os.rename(rdf_file, new_rdf_file)

    # Move .rdf and .tga files to old_out folder
    for file in os.listdir("temp"):
        if file.endswith(".tga") or file.endswith(".rdf"):
            shutil.move(os.path.join("temp", file), old_out_folder)

    # Clean temp folder
    clean_temp_folder()

def build_xpr():
    # Scan for folders in new_in
    new_in = "new_in"
    folders = [f for f in os.listdir(new_in) if os.path.isdir(os.path.join(new_in, f))]

    if not folders:
        print("No folders found in 'new_in' folder.")
        return

    print("Found the following folders:")
    for i, folder in enumerate(folders):
        print(f"[{i + 1}] {folder}")
    choice = int(input("Type the number of the folder you want to build from: ")) - 1
    selected_folder = folders[choice]

    # Copy contents of the selected folder to temp folder
    folder_path = os.path.join(new_in, selected_folder)
    for item in os.listdir(folder_path):
        shutil.copy(os.path.join(folder_path, item), "temp")

    # Check if .rdf file exists
    rdf_files = [f for f in os.listdir("temp") if f.endswith(".rdf")]
    if not rdf_files:
        print("No XPR2 TOC found.")
        clean_temp_folder()
        return

    rdf_file = rdf_files[0]

    # Run Bundler.exe with the .rdf file
    subprocess.run(["temp\\Bundler.exe", rdf_file], cwd="temp")

    # Move new .xpr to new_out folder
    xpr_file = f"{os.path.splitext(rdf_file)[0]}.xpr"
    if os.path.exists(os.path.join("temp", xpr_file)):
        shutil.move(os.path.join("temp", xpr_file), os.path.join("new_out", xpr_file))

    # Clean temp folder
    clean_temp_folder()

def main():
    print("Are you dumping or building an .XPR file?")
    print("For dumping type [1] and for building type [2].")
    choice = input("Your choice: ")

    if choice == "1":
        dump_xpr()
    elif choice == "2":
        build_xpr()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
