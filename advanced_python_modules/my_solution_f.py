"""
This module will be used to hold the code that solves the advanced modules puzzle
"""

# Step 1 Unzip Instructions:
import zipfile
instructions = zipfile.ZipFile('unzip_me_for_instructions.zip', 'r')
instructions.extractall('the_content')

# Step 2 Read Instruction  file contents:
file = open('C:\\DevEx\\IdeaProjects\Python.Udemy.Complete_Python_BootCamp\\advanced_python_modules'
            '\\08-Advanced-Python-Module-Exercise\\the_content\\extracted_content\\instructions.txt', 'r')
print(file.read())

# Step 3 Read files in folder:
print('\n')
print('The solution starts here: ')
import os

file_path = 'C:\\DevEx\\IdeaProjects\\Python.Udemy.Complete_Python_BootCamp\\advanced_python_modules\\08-Advanced-Python-Module-Exercise\\extracted_content'
for folder, sub_folders, files in os.walk(file_path):
    print(f'Currently loooking at {folder}')
    print('\n')
    print('The subdfolders are:')
    for sub_fold in sub_folders:
        print(f"Subfolder: {sub_fold}")
    print('\n')
    print("the files are: ")
    for f in files:
        import re
        pattern = r'\d{3}-\d{3}-\d{4}'
        fileName = os.path.join(folder, f)
        with open(fileName, 'r') as the_file:
            the_lines = the_file.read()
            result = re.search(pattern, the_lines)
            print(result)
            print(f'Files: {f}')

    print('\n')



print('\n')
