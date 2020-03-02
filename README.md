# Archiver - A simple directory archiving utility

An easy to use utility that condenses directories into a single file. Its functionality is very similar to zipping a folder. This program is written entirely in Python and uses no external libraries. Archived files are compressed using the bzip2 standard to take up less space than the actual directory itself.

Usage:

    * Clone the repository with:
    git clone https://github.com/naraklol/archiver

    * Move the directory to be archived into the cloned repository

    * Run the command:
    python3 archiver.py [option] [target]

    [option] = -u (unarchive), -a (archive)
    [target] = directory to be archived (if archiving) or archived file (if unarchiving)

Known bugs:

    * Single files cannot currently be archived.
    * Any file with the content "DIRECTORY:" or "FILE:" may cause errors.
