#Report

import csv

def write_csv_report(scored_files,output_path):
    """
    Purpose: write a ranked report using the scores in csv
    Parameters: the scored files and the string to the path to deposit the csv
    Returns: N/A - writes the csv
    """
    fieldnames=["Path","Name","Size","Date Modified","Score"]

    with open(output_path,"w",newline="",encoding="utf-8") as csv_file:
        writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writeheader()

        for record in scored_files:#so it doesn't get overwritten
            row={
                "Path": record["Path"],
                "Name": record["Name"],
                "Size": record["Size"],
                "Date Modified": record["Date Modified"],
                "Score": record["Score"]
            }
            writer.writerow(row)