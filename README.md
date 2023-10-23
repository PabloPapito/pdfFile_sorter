# pdfFile_sorter

Program Description
This program is used to verify the contents of PDF files. If a file does not have the number of pages specified by the user, the program will move that file to a subfolder specified by the user and delete the original version of the file from the main folder.

I wrote the program in Python programming language and used the PyPDF2 library to manipulate PDF files.

Instructions
To run the program, follow these steps:

- When prompted, enter the path to the folder containing the PDF files to be examined.
- When prompted, enter the path to the folder where you want to store files with the selected number of pages.
- When prompted, enter the number of pages you want to check for in the files.
- Run the program.
After running the program, it will iterate through all the files located in the folder specified by the user and move files that do not have the selected number of pages to the folder specified by the user.

Note: The program permanently removes the original version of the file from the main folder, so be sure to make a backup of any files you want to test.

Requirements
The program requires the PyPDF2 library to be installed.

You can install it using the pip install PyPDF2 command -> (win + cmd).
