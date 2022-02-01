import zipfile
import os

# The list of file types to be included which might be important(optional)
extensions = ["html", "py", "docx", "pdf", "exe", "xlsx", "xls"]

Zippy = zipfile.ZipFile("Backup.zip", 'w')

for folder, subfolders, file in os.walk("C:\\Logadheep\\Notes\\ADP\\"):
    for subfolder in subfolders:
        path = folder + subfolder
    for x in file:
        # To Backup only certain filetypes
        for i in extensions:
          	if x.endswith(i):
        		filepath = folder + "\\" + x
        		print(filepath)
        		Zippy.write(filepath, compress_type=zipfile.ZIP_DEFLATED)
Zippy.close()
