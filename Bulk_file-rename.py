import os
import datetime

# Function to list all files in the given directory
def list_files_in_directory(directory):
    """
    Lists all files in the specified directory.
    """
    print(f"\nListing files in directory: {directory}\n")
    files = os.listdir(directory)
    if not files:
        print("The directory is empty.")
    else:
        for i, filename in enumerate(files, 1):
            print(f"{i}. {filename}")
    print("\n")

# Function to exclude files based on a pattern
def exclude_files(files, pattern):
    """
    Excludes files that contain the given pattern.
    """
    return [f for f in files if pattern not in f]

# Function to generate a new filename based on user input
def generate_new_filename(filename, prefix='', suffix='', replace_str='', new_str='', num=None, timestamp=False):
    """
    Generates a new filename based on the given options: prefix, suffix, string replacement, and numbering.
    """
    new_filename = filename

    # Replace part of the filename if requested
    if replace_str and new_str:
        new_filename = new_filename.replace(replace_str, new_str)

    # Add prefix if provided
    if prefix:
        new_filename = prefix + new_filename

    # Add suffix if provided
    name, ext = os.path.splitext(new_filename)
    if suffix:
        new_filename = f"{name}{suffix}{ext}"

    # Add numbering if requested
    if num is not None:
        new_filename = f"{prefix}{num:03}{suffix}{ext}"

    # Add date and time stamp if requested
    if timestamp:
        current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        new_filename = f"{name}_{current_time}{ext}"

    return new_filename

# Function to rename files
def rename_files(directory, files, new_filenames, log_filename="rename_log.txt"):
    """
    Renames files in the given directory and writes a log of the changes.
    """
    log_entries = []
    
    for old_name, new_name in zip(files, new_filenames):
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name)
        
        os.rename(old_path, new_path)
        log_entries.append(f"Renamed: {old_name} -> {new_name}\n")

    # Write the renaming log to a file
    with open(log_filename, "a") as log_file:
        log_file.writelines(log_entries)

    print(f"\nRenaming complete! Log saved to {log_filename}\n")

# Function to preview renaming changes
def preview_renaming(files, new_filenames):
    print("\nPreview of renaming:")
    for old_name, new_name in zip(files, new_filenames):
        print(f"{old_name} -> {new_name}")
    confirm = input("\nProceed with renaming? (y/n): ").lower()
    return confirm == 'y'

def main():
    print("Bulk File Renamer")

    directory = input("Enter the path to the directory containing the files: ").strip()
    if not os.path.exists(directory):
        print("The directory does not exist.")
        return

    # List the files in the directory
    list_files_in_directory(directory)

    # New feature: Exclude specific files
    exclude_pattern = input("Enter a pattern to exclude files (or leave blank): ").strip()
    
    # List of files after exclusion
    files = os.listdir(directory)
    if exclude_pattern:
        files = exclude_files(files, exclude_pattern)

    # Options for renaming
    prefix = input("Enter a prefix to add (or leave blank): ").strip()
    suffix = input("Enter a suffix to add (or leave blank): ").strip()
    replace_str = input("Enter a part of the filename to replace (or leave blank): ").strip()
    new_str = input(f"Enter the new string to replace '{replace_str}' (or leave blank): ").strip() if replace_str else ''
    
    num_choice = input("Do you want to number the files sequentially? (y/n): ").strip().lower()
    start_num = int(input("Enter the starting number: ").strip()) if num_choice == 'y' else None

    timestamp_choice = input("Do you want to add a date and time stamp? (y/n): ").strip().lower()
    timestamp = timestamp_choice == 'y'

    # Generate new filenames
    new_filenames = [generate_new_filename(f, prefix, suffix, replace_str, new_str, start_num, timestamp) for f in files]

    # Preview renaming
    if preview_renaming(files, new_filenames):
        rename_files(directory, files, new_filenames)
    else:
        print("Renaming canceled.")

if __name__ == "__main__":
    main()
