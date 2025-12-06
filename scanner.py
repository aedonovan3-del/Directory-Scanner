#Scanner

import os
from datetime import datetime

def scan_directory(root_path):
    """
    Purpose: scans the directory
    Parameters: string for the directory path
    Returns: file metadata
    """

    file_list=[]

    for dir_path,dir_names,file_names in os.walk(root_path):
        for file_name in file_names:
            full_path = os.path.join(dir_path,file_name)

            try:
                stats=os.stat(full_path)
            except (FileNotFoundError,PermissionError):
                continue#avoid missing files and permissions issues    

            file_info={
                "Path":full_path,
                "Name":file_name,
                "Size":stats.st_size,
                "Date Modified":datetime.fromtimestamp(stats.st_mtime)
            }    
            file_list.append(file_info)

    return file_list            


