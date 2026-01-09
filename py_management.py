import os
import keyboard
# -------- file management functions --------

def change_directory(event, path):
    try:
        print("input the path you want to change too!")
        input_path = input("Enter path:")
        os.chdir(input_path)
        print(f"changed directory too: {input_path}")
    except FileNotFoundError:
        print("Error: ! the path was not found.")


def list_files_in_path():
    file_list = os.listdir(".")
    print("Files in the current directory:")
    for file_name in file_list:
      print(file_name)

def create_directory(dir_name):
    try:
        print("input a name for the directory!")
        input_name = input("Enter:")
        os.makedirs(input_name)
        print(f"Directory '{input_name}' created successfully")
    except FileNotFoundError:
        print("Error: ! the path was not found.")

def remove_directory(dir_name):
    try:
        print("input a name for the directory to remove!")
        input_name = input("Enter:")
        os.rmdir(input_name)
        print(f"Directory '{input_name}' removed successfully")
    except FileNotFoundError:
        print("Error: ! the path was not found.")

def rename_directory(old_name, new_name):
    try:
        print("input the current name of the directory!")
        input_old_name = input("Enter current name:")
        print("input the new name for the directory!")
        input_new_name = input("Enter new name:")
        os.rename(input_old_name, input_new_name)
        print(f"Directory '{input_old_name}' renamed to '{input_new_name}' successfully")
    except FileNotFoundError:   
        print("Error: ! the path was not found.")

def open_file(file_name):
    try:
        print("input the file name to open!")
        input_name = input("Enter file name:")
        with open(input_name, "r") as file:
            content = file.read()
            print(f"Content of '{input_name}':\n{content}")
    except FileNotFoundError:
        print("Error: ! the file was not found.")

def remove_file(file_name):
    try:
        print("input the name of the file to remove !")
        input_name = input("Enter file name:")
        os.remove(input_name)
        print(f"File '{input_name}' removed successfully")
    except FileNotFoundError:   
        print("Error: ! the file was not found.")

# -------- function working examples --------

# -------- main menu ---------
keybind_list = {"A": "Change directory", "B": "List files in path", "3.": "Git", "4.": "System Info", "5.": "Change Username", "6.": "Exit"}
print("File Management System")
keyboard.add_hotkey('a+1', change_directory)
keyboard.wait('esc')
# -------- working progress ---------

#create_directory(dir_name="")
#rename_directory(old_name="", new_name="")
#remove_file(file_name="")
list_files_in_path()
