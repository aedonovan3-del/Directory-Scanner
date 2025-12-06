#run
import os
from scanner import scan_directory
from analyzer import analyze_files
from scorer import score
from report import write_csv_report

def run(root_path):
    """
    Purpose: run the modules
    Parameters: string for the path to the directory
    Returns: writes the report of the potential automation candidates to a csv file
    """    
    weights = [0.0,0.001,-0.1,1.0]#bias,size,days since mod,extension score

    files = scan_directory(root_path)
    analyzed = analyze_files(files)
    scored = score(analyzed,weights)

    #report
    output_csv = "automation_candidates.csv"
    write_csv_report(scored,output_csv)
    print(f"Report written to {os.path.abspath(output_csv)}")

if __name__ == "__main__":
    folder = input("Enter directory to scan (blank = current directory): ").strip()

    if not folder:
        folder = os.getcwd()

    run(folder)
