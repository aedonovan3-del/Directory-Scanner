#Analyzer

import os
from datetime import datetime

#placeholder map to prioritize automation candidate likelies
ext_scores = {
    ".accdb": 10,
    ".xlsx": 9,
    ".xlsm": 9,
    ".xls": 8,
    ".csv": 7,
    ".txt": 6,
    ".json": 5,
    ".xml": 5,
    ".pdf": 4,
    ".png": 2,
    ".jpg": 2,
    ".jpeg": 2,
    ".gif": 1,
    ".mp4": 1,
    ".mov": 1,
    ".wav": 1
}

def analyze_files(file_list):
    """
    Purpose: analyze the file metadata
    Parameters: file_list (metadata dictionaries)
    Returns: 
    """
    analyzed_files = []
    now = datetime.now()

    for record in file_list:
        size_kb = record["Size"]/1024.0
        since_mod = (now-record["Date Modified"]).days

        _, ext = os.path.splitext(record["Name"])
        ext_score = ext_scores.get(ext.lower(),0)#automatically 0 if ext isn't in map

        attributes = [size_kb,since_mod,ext_score]

        new_record=dict(record)
        new_record["Attributes"] = attributes
        analyzed_files.append(new_record)
        
    return analyzed_files        
