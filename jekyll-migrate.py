import os
from functools import reduce
import re
frontMatter = "--- ---"
localDir = input('Enter exact path: ')
directory = "C:\\Users\\lucar\\Downloads\\"+ localDir +"\\"


def create_md_from_dir(rootdir):
    if os.access("./output/" + localDir, os.R_OK):
        print("Folder ok!")
    else:
        os.mkdir("./output/" + localDir)
        print("Folder created!")
    for root, dirs, files in os.walk(rootdir):
        rootdir = rootdir.rstrip(os.sep)
        start = rootdir.rfind(os.sep) + 1
        folders = root[start:].split(os.sep)
        for name in files:
            i = 0
            i += 1
            fileContent = "---"+ "\n"+ "title: " + name[:-4] + "\n" + "image: " + name + "\n"  + "brand: " + str(folders[1]) + "\n" + "layout: vestito" +"\n" +"---"
            cleanName = name.replace(" ", "")
            cleanName = cleanName[:-4]
            fileName = ".\\output\\" + localDir +  "\\" + cleanName + ".md"
            with open(fileName, 'w') as outfile:
                outfile.write(str(fileContent))
    print("Files Written")
create_md_from_dir(directory)
