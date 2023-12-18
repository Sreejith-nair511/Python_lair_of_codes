#to backkup a file into zip file 

from zipfile import ZipFile
import os

extension=input('input extesnion')
zippy=ZipFile('backup.zip','w')
for folder,subfolder,file in os.walk('C:\pyyton\londo'):
    for subfolder in subfolder:
        path=folder+subfolder
        for x in file:
            if x.endswith(extension):
                filepath = folder + "\\" + x
                print(filepath)
                zippy.write(filepath, compress_type=ZipFile.ZIP_DEFLATED)
                zippy.close()



