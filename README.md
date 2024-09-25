# File Sorting Program

## Overview
The File Sorting Program is a Python script that helps users automatically sort files in a specified folder into subfolders based on their file extensions. The program creates new directories for common file types such as PDF, DOC(X), JPG, PNG, and CSV and moves files into their corresponding folders. It also provides a summary report of the sorting process.

## How It Works
- Prompts the user to enter the path of the folder they wish to organize.
- Automatically creates new subfolders for different file types (PDF, DOC(X), JPG, PNG, CSV).
- Copies files into the corresponding subfolders based on their extension.
- Displays real-time feedback on successfully sorted files and unsupported file types.
- Outputs a final report summarizing the total number of files sorted by type and any unsupported files.

## Key Features
- **Automatic Folder Creation**: Creates folders for each file type, if not already present.
- **Real-time Feedback**: Notifies users of each file that has been successfully sorted.
- **Comprehensive Report**: At the end of the operation, a detailed report of the number of files sorted by type is displayed, along with any files that could not be sorted.
- **Supports Multiple File Types**: Supports sorting of `.pdf`, `.doc`, `.docx`, `.jpg`, `.png`, `.csv`, and `.xls` file extensions.

## How to Run
1. Clone the repository from GitHub.
2. Run the script in a Python environment.
3. Enter the path of the folder you want to sort when prompted.
4. The program will organize the files into corresponding subfolders and display a summary of the results.

## Requirements
- Python 3.x
- `shutil` and `os` modules (part of Python's standard library)

## Future Improvements
- Add support for additional file types.
- Include a feature to handle files with duplicate names.
- Implement error handling for cases where folder creation fails.

## Author
Maksym Pozomin
