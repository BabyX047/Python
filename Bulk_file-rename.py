import os

def rename_files(directory, prefix='', suffix='', replace_str='', new_str='', start_num=None):
    """
    Renames files in a given directory with options for adding prefixes, suffixes, replacing parts of filenames, or numbering.
    
    Parameters:
    - directory: Path to the directory containing the files
    - prefix: A string to add as a prefix to each file (optional)
    - suffix: A string to add as a suffix to each file (optional)
    - replace_str: String in filenames to be replaced (optional)
    - new_str: The new string to replace 'replace_str' (optional)
    - start_num: Optional, for numbering files starting from this value (optional)
    """
    # List all files in the directory
    files = os.listdir(directory)
    
    # Track the number for sequential renaming if provided
    num = start_num if start_num is not None else None
    
    for filename in files:
        # Skip directories, only rename files
        if os.path.isfile(os.path.join(directory, filename)):
            # Create the new filename
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
                new_filename = f"{prefix}{num:03}{suffix}{ext}"  # Zero-padded numbering (e.g., 001, 002, 003)
                num += 1

            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f'Renamed: {filename} -> {new_filename}')

def main():
    print("Bulk File Renamer")
    
    # User input for directory
    directory = input("Enter the path to the directory containing the files: ").strip()
    
    if not os.path.exists(directory):
        print("The directory does not exist.")
        return
    
    # Options for renaming
    print("\nOptions:")
    prefix = input("Enter a prefix to add (or leave blank): ").strip()
    suffix = input("Enter a suffix to add (or leave blank): ").strip()
    replace_str = input("Enter a part of the filename to replace (or leave blank): ").strip()
    new_str = input(f"Enter the new string to replace '{replace_str}' (or leave blank): ").strip() if replace_str else ''
    
    # Optional numbering
    num_choice = input("Do you want to number the files sequentially? (y/n): ").strip().lower()
    start_num = None
    if num_choice == 'y':
        start_num = int(input("Enter the starting number: ").strip())
    
    # Call the renaming function
    rename_files(directory, prefix, suffix, replace_str, new_str, start_num)
    print("Renaming complete!")

if __name__ == "__main__":
    main()
