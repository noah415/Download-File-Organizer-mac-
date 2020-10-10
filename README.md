# Download-File-Organizer-mac-
This is a simple python script that allows you to organize any folder in your mac that you want. The script is currently written to organize the /Downloads folder; however, you may change the path to whatever directory you would like to organize. There are also instructions that It works best when files are downloaded from Safari. Enjoy!



# Instructions for Automator Setup
## Step 1
* open Automator
## Step 2
* select "New Document" in the bottom left
## Step 3
* choose the "Folder Action" Document Type
## Step 4
* in the library drop down, select "Utilities", then drag "Run Shell Script" into the blank workflow section
* or
* search in the search bar, "Run Shell Script", then drag "Run Shell Script" into the blank workflow section
## Step 5
* make sure the "Shell:" drop down is selected to "/bin/bash"
## Step 6
(this is the path to the execute python command and the path to where you keep the organize1.py)
* type this in the shell --> "/usr/local/bin/python3 /your/path/to/organizer/script"
## Step 7
* save the Automator Action
