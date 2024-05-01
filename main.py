import shutil
import os

path = input("Enter the path: ")  # Prompting the user to indicate the path of the folder they want to sort

dir_pdf = (os.path.join(path, 'PDF files'))     # Creates
dir_doc = (os.path.join(path, 'DOC(X) files'))  # Paths
dir_jpg = (os.path.join(path, 'JPG files'))     # For
dir_png = (os.path.join(path, 'PNG files'))     # Future
dir_csv = (os.path.join(path, 'CSV files'))     # Folders

os.mkdir(dir_pdf)  # Creates folders
os.mkdir(dir_doc)  # For different
os.mkdir(dir_jpg)  # Extensions
os.mkdir(dir_png)
os.mkdir(dir_csv)


count_pdf = 0  # Counter for the report at the end
count_doc = 0
count_jpg = 0
count_png = 0
count_csv = 0
count_failed = 0

files = os.listdir(path)

for file in files:  # Main sorting mechanism
    file_name, file_ext = os.path.splitext(file)  # Extracts the file extension
    if file_ext == '.pdf':
        shutil.copy(os.path.join(path, file), dir_pdf)  # Creates a copy in the new folder
        count_pdf += 1  # Updates the counter
        print("Successfully sorted PDF")  # Gives feedback

    elif file_ext == '.doc' or file_ext == '.docx':
        shutil.copy(os.path.join(path, file), dir_doc)
        count_doc += 1
        print("Successfully sorted DOC(X)")

    elif file_ext == '.jpg':
        shutil.copy(os.path.join(path, file), dir_jpg)
        count_jpg += 1
        print("Successfully sorted JPG")

    elif file_ext == '.png':
        shutil.copy(os.path.join(path, file), dir_png)
        count_png += 1
        print("Successfully sorted PNG")

    elif file_ext == '.csv' or file_ext == '.xls':
        shutil.copy(os.path.join(path, file), dir_csv)
        count_csv += 1
        print("Successfully sorted CSV")

    else:
        count_failed += 1
        print("Unsupported Extension")

print("\nSorting report:")
print(f"Total PDFs: {count_pdf}")
print(f"Total DOC(X)s: {count_doc}")
print(f"Total JPGs: {count_jpg}")
print(f"Total PNGs: {count_png}")
print(f"Total CSVs: {count_csv}")
print(f"Total failures: {count_failed-5}")
