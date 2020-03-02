import os
import sys
import shutil
import bz2

def archive():

    # get the correct working directory and the path
    # of the to be compressed directory
    path = os.getcwd()
    archiveName = sys.argv[2]
    dirPath = path + "/" + archiveName

    # check if the directory provided is valid
    if not os.path.isdir(dirPath):
        print("Directory provided is not an actual directory")
        exit()

    # check if the archive already exists and remove it
    if os.path.isfile(dirPath + ".arch"):
        os.remove(dirPath + ".arch")

    # empty string for adding data to be archived
    archiveData = b""

    # iterate through each sub directory and list all files
    for (dirpath, dirnames, filenames) in os.walk(dirPath):

        # add directory tag to archive
        archiveData += ("DIRECTORY: " + dirpath + "\n").encode()

        # iterate through each file in the subdirectory
        for filename in filenames:

            # add file tag to archive
            archiveData += ("FILE: " + filename + "\n").encode()

            # open the file and add it to the archive
            file = open(dirPath + '/' + filename, 'rb')
            archiveData += file.read()

    # compress
    compressedData = bz2.compress(archiveData)

    # open an archive file to write in
    archive = open(archiveName + ".arch", 'wb')
    archive.write(compressedData)

def unarchive():

    # get the currect working directory and the path
    # of file to be unarchived
    path = os.getcwd()
    archiveName = sys.argv[2]
    dirPath = path + "/" + archiveName

    # check if the archive exists
    if not os.path.isfile(dirPath):
        print("Archive does not exist in current directory")
        exit()

    # check if the file provided is an archive
    if archiveName.split('.', 1)[1] != "arch":
        print("File provided is not an archive in current directory")
        exit()

    # check if unarchived directory already exists
    if os.path.isdir(dirPath.split('.', 1)[0]):
        inp = input("Directory with same name already exists. Overwrite? (y/n) ")
        if inp == "y" or inp =="yes":
            shutil.rmtree(dirPath.split('.', 1)[0])
        if inp == "n" or inp =="no":
            exit()

    # open the archive and read data
    archive = open(dirPath, 'rb')
    buf = bz2.decompress(archive.read()).decode()

    #split data into directories
    directorySplit = buf.split("DIRECTORY: ")
    directorySplit.pop(0)

    # go through each directory
    for directory in directorySplit:

        # reattach the directory label
        directory = "DIRECTORY: " + directory

        # split each directory into its files
        files = directory.split("FILE: ")

        # extract the directory name and create it
        newDir = files.pop(0)[11:-1]
        os.mkdir(newDir)

        # go through each file
        for file in files:

            # split each file into its filename and contents
            fileSplit = file.split('\n', 1)

            #create a new file and write the archived data
            newFile = open(newDir + '/' + fileSplit[0], 'wb')
            newFile.write(fileSplit[1].encode())



def main():

    # check for correct number of arguments provided
    if len(sys.argv) != 3:
        print("Incorrect number of arguments provided.\n\n \
        Usage: python3 zip.py [option] [directory]\n\n\
        [option] = -u: unarchive, -a: archive")
        exit()

    # options for the program to run
    if sys.argv[1] == "-u" or sys.argv[1] == "unarchive":
        unarchive()
    if sys.argv[1] == "-a" or sys.argv[1] == "archive":
        archive()

main()
