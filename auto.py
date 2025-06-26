import os
import shutil

# Path to your Downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

def organize():
    for file in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()

            # Skip files without extension
            if not ext:
                continue

            # Folder name based on extension (e.g., ".pdf" → "PDF")
            folder_name = ext[1:].upper() + " Files"
            target_folder = os.path.join(downloads_folder, folder_name)

            # Create folder if it doesn't exist
            os.makedirs(target_folder, exist_ok=True)

            # Move file
            shutil.move(file_path, os.path.join(target_folder, file))
            print(f"Moved: {file} → {folder_name}")

if __name__ == "__main__":
    organize()
