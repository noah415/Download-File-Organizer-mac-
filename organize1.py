#import libraries
from os import listdir
from os.path import isfile, join
import os
import shutil




'''
Sorting files in a folder (downloads)
'''

def sort_files_in_downloads(downloads_path):

    files = [f for f in listdir(downloads_path) if isfile(join(downloads_path, f))]

    #creating preexisting list of file types
    file_type_variation_list = ["jpeg", "jpg", "tiff", "giff", "bmp", "png", "bpg", "svg", "heif", "psd", 
                                "avi", "flv", "wmv", "mov", "mp4", "webm", "vob", "mng", "qt", "mpg", "mpeg", 
                                "3gp", "mkv", "oxps", "epub", "pages", "docx", "doc", "fdf", "ods",
                                "odt", "pwi", "xsn", "xps", "dotx", "docm", "dox", "rvg", "rtf", "rtfd", "wpd", 
                                "xls", "xlsx", "ppt", "pptx", "a", "ar", "cpio", "iso", "tar", "gz", "rz", "7z",
                                "dmg", "rar", "xar", "zip", "aac", "aa", "aac", "dvf", "m4a", "m4b", "m4p", "mp3",
                                "msv", "ogg", "oga", "raw", "vox", "wav", "wma", "txt", "in", "out", "pdf"]

    #creating preexisting dictionary
    file_type_folder_dict = {}

    file_type_dict = {
        'images': ["jpeg", "jpg", "tiff", "gif", "bmp", "png", "bpg", "svg",
                    "heif", "psd"],
        'videos': ["avi", "flv", "wmv", "mov", "mp4", "webm", "vob", "mng",
                    "qt", "mpg", "mpeg", "3gp", "mkv"],
        'documents': ["oxps", "epub", "pages", "docx", "doc", "fdf", "ods",
                    "odt", "pwi", "xsn", "xps", "dotx", "docm", "dox",
                    "rvg", "rtf", "rtfd", "wpd", "xls", "xlsx", "ppt",
                    "pptx"],
        'archives': ["a", "ar", "cpio", "iso", "tar", "gz", "rz", "7z",
                    "dmg", "rar", "xar", "zip"],
        'audio': ["aac", "aa", "aac", "dvf", "m4a", "m4b", "m4p", "mp3",
                    "msv", "ogg", "oga", "raw", "vox", "wav", "wma"],
        'plaintext': ["txt", "in", "out"],
        'pdf': ["pdf"]
    }

    for file in files:

        file_type_list = file.split(".")
        file_type = file_type_list[-1]


        #also not allowing .DS_Store to be messed with 
        if file_type == "DS_Store":
                continue
        
        #checks if file neeeds to be put in "other" directory and creates all new directories
        else:
            if file_type not in file_type_variation_list:
                file_type = "other"
            else:
                for key in file_type_dict:
                    if file_type in file_type_dict[key]:
                        file_type = key

            new_folder_name = downloads_path + "/" + file_type
            file_type_folder_dict[str(file_type)] = str(new_folder_name)

            if os.path.isdir(new_folder_name) == True:
                continue
            else:
                os.mkdir(new_folder_name)



#moves files into their respective directories
    for file in files:

        
        src_path = downloads_path + "/" + file
        file_type_list = file.split(".")
        file_type = file_type_list[-1]

        if file_type == "DS_Store":
            continue

        else:
            if file_type not in file_type_variation_list:
                file_type = "other"

            else:
                for key in file_type_dict:
                    if file_type in file_type_dict[key]:
                        file_type = key
            print(file_type)
            dest_path = file_type_folder_dict[str(file_type)]
            shutil.move(src_path, dest_path)
            print(src_path + " >>> " + dest_path)

    if len(files) == 1 and '.DS_Store' in files or len(files) == 0:
        print("\nNo organization needed. :)")
        print("\n")

    else:
        print("\nThere were " + str(len(files)) + " files organized!")
        print("\n")

    
    

if __name__=="__main__":
    #change this PATH to whatever folder you want to be organized
    downloads_path = "/Users/noah/Downloads"
    #                ^^^^^^^^^^^^^^^^^^^^^^^
    
    sort_files_in_downloads(downloads_path)