import os

def create_readme_files(root_dir):
    """
    Walk through the directory tree and add a README.md file to each folder.

    Args:
        root_dir (str): Path to the root directory where README files should be created.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        readme_path = os.path.join(dirpath, 'README.md')
        
        if not os.path.exists(readme_path):
            try:
                with open(readme_path, 'w') as readme_file:
                    readme_file.write(f"# {os.path.basename(dirpath)}\n\n")
                    readme_file.write(f"This folder is located at `{dirpath}`.\n\n")
                    readme_file.write("Feel free to provide additional details here.")
                print(f"Created README.md in {dirpath}")
            except Exception as e:
                print(f"Error creating README.md in {dirpath}: {e}")
        else:
            print(f"README.md already exists in {dirpath}, skipping.")

if __name__ == "__main__":
    # Set the directory where README.md files should be added
    root_directory = os.getcwd()  # Change this to any specific directory you want to target

    create_readme_files(root_directory)
    print("Process complete!")