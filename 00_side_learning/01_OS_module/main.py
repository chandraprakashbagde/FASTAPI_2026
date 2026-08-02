import os
### 1. Working With the Current Directory
# print(dir(os))

## Get Current working directory
# print(os.getcwd())

## Change working directory
# os.chdir("/Users/chandraprakashrameshbagade/")
# print(os.getcwd())

### 2. File and Directory Management
## Cerate, delete, rename and modify files and directories

# Make Single dir
# os.mkdir("newforlder")
## os.mkdir("newfolder/dops") this will does not works

# Make multiple dir
# os.makedirs("test/2016")

## Remove File
# os.remove("test/test.txt")

## Remove single empty directory
# os.rmdir("test")

## Remove directory + empty parent directoreis
# os.removedirs("test/test1")

## Get List of directories?
# print(os.listdir("test")) # Privides the list of all folders inside the passed directory name
# allDirsAndFiles = os.walk("test")
# for d in allDirsAndFiles:
#     print(d)

## get status
# print(os.stat("test/test1/test1.py"))

path = "a8d81cd9-3c75-40f1-8457-e635ecb2d8d9/aadhar_files"
allDirsAndFiles = os.walk(path)

for filename in next(allDirsAndFiles)[2]:
    os.remove(f"{path}/{filename}")