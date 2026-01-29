import os
import keyboard
from py import Observable as key_pass
import time

class ApplicationCore:

# -------- file management functions --------

     def change_directory(self, event, path):
      try:
        print("input the path you want to change too!")
        input_path = input("Enter path:")
        os.chdir(input_path)
        print(f"changed directory too: {input_path}")
        keyboard.wait('esc')
      except FileNotFoundError:
       print("Error: ! the path was not found.")
      except KeyboardInterrupt:
       print("Going back to main menu")
     

     def list_files_in_path(self, event, list):
      file_list = os.listdir(".")
      print("Files in the current directory:")
      for file_name in file_list:
       print(file_name)
    
     def create_directory(self, event, dir_name):
      try:
          print("input a name for the directory!")
          input_name = input("Enter:")
          os.makedirs(input_name)
          print(f"Directory '{input_name}' created successfully")
      except FileNotFoundError:
         print("Error: ! the path was not found.")

     def remove_directory(self, event, dir_name):
      try:
          print("input a name for the directory to remove!")
          input_name = input("Enter:")
          os.rmdir(input_name)
          print(f"Directory '{input_name}' removed successfully")
      except FileNotFoundError:
         print("Error: ! the path was not found.")

     def rename_directory(self, event, old_name, new_name):
      try:
         print("input the current name of the directory!")
         input_old_name = input("Enter current name:")
         print("input the new name for the directory!")
         input_new_name = input("Enter new name:")
         os.rename(input_old_name, input_new_name)
         print(f"Directory '{input_old_name}' renamed to '{input_new_name}' successfully")
      except FileNotFoundError:   
         print("Error: ! the path was not found.")

     def open_file(self, file_name):
      try:
         print("input the file name to open!")
         input_name = input("Enter file name:")
         with open(input_name, "r") as file:
            content = file.read()
            print(f"Content of '{input_name}':\n{content}")
      except FileNotFoundError:
        print("Error: ! the file was not found.")

     def remove_file(self, event, file_name):
      try:
         print("input the name of the file to remove !")
         input_name = input("Enter file name:")
         os.remove(input_name)
         print(f"File '{input_name}' removed successfully")
      except FileNotFoundError:   
         print("Error: ! the file was not found.")


# ------- working kind of ---------

# -----------------------------------

# -------- function working examples --------

# -------- main menu ---------
     def main_menu(self): 
      while True:  # making a loop
       try:  # used try so that if user pressed other than the given key error will not be shown
          if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
          if keyboard.is_pressed('a'):
            self.change_directory()
            break  # finishing the loop
       except:
        break
      keybind_list = { 
            'A': "Change directory", 
            'B': "List files in path", 
            'C': "Create Directory", 
            'D': "Remove Directory", 
            '5': "Change Username", 
            '6': "Exit" 
        }
      exec = {
       self.change_directory(event="", path="")
      }
      print("File Management System")
      for key, action in exec():
       print({key},{action})
# -------- working progress ---------

#create_directory(dir_name="")
#rename_directory(old_name="", new_name="")
#remove_file(file_name="")
if __name__ == "__main__":
 app = ApplicationCore()

 app.main_menu()
    
