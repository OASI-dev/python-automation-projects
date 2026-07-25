import os
import shutil

folder_path = "test_folder"

category_map = {
    ".pdf" : "PDFs",
    ".jpg" : "Images",
    ".jpeg" :"Images",
    ".png" : "Images",
    ".gif" : "Images",
    ".txt" : "Documents",
    ".docs" : "Documents",
    ".doc" : "Documents",
    ".mp3" : "Audio",
    ".wav" : "Audio",
    ".csv" : "Spreadsheets",
    ".xlsx" : "Spreadsheets",
    ".exe" : "Executables"
}

def main():
    for filename in os.listdir(folder_path):
        source_path = os.path.join(folder_path,filename)

        if not os.path.isfile(source_path):
            continue

        _,extension = os.path.splitext(filename)
        extension = extension.lower()

        category = category_map.get(extension,"other")

        destination_folder = os.path.join(folder_path,category)
        os.makedirs(destination_folder,exist_ok = True)

        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path,destination_path)

        print(f"Moved {filename} -> {category}/")

if __name__ == "__main__":
    main()