############################################
#Automatisierungsskript zum kopieren von
#Arbeitsdaten auf meinen NAS
############################################
import os
import shutil

root = "D:\\Os"
destination = "U:\\Os"
path = os.path.join(root, "target")


for path, subdirs, files in os.walk(root):
    for name in files:
        print(os.path.join(path, name))
        shutil.copy2(os.path.join(path, name), destination + "\\" + name)

