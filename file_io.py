# This script is going to create folder and file using pathlib and shutil

# Importing the necessary modules
import pathlib, shutil

# getting the working directory as an object
working_directory = pathlib.Path.cwd()

# printing the working directory
print(working_directory)

# creating an object with the parent directory
py_path = working_directory.parent

# Creating a folder called "folder_week11" in the parent directory
folder_week11 = py_path/"folder_week11"

# Making the directory if it is not already created
folder_week11.mkdir(exist_ok= True)

#Creating a text file called "week11.txt"
week11 = folder_week11/"week11.txt"

# Using the touch function creating the txt file in the directory
week11.touch()

# Using the write function writing to the text file
with week11.open(mode= "w", encoding= "utf-8") as file:
    file.write("Test: Writing to file.")
  
# reading what was written and printing it out 
with week11.open(mode= "r", encoding= "utf-8") as file:
    print(file.read())

# Creating a backup folder in the parent directory
file_backups = folder_week11/"file_backups"

file_backups.mkdir(exist_ok= True)

# Creating a backup txt file called "file_backups.txt"
week11_backup = file_backups/"file_backups.txt"

# Copying what was in the week11.txt file into the file_backups file
shutil.copy2(week11, week11_backup)

# Printing out the text files in the folder folder_week11
for item in folder_week11.rglob("*.txt"):
    print(item.stem)