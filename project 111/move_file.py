import os
import shutil

from_dir="C:/Users/91976/Desktop/Downloads"
to_dir="C:/Users/91976/Desktop/Document_Files"

list_of_files=os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
    file,ext=os.path.splitext(i)
    print(file,ext)
