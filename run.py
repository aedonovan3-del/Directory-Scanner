#run

from scanner import scan_directory
from analyzer import analyze_files
from scorer import score
from report import write_csv_report

def run():
    root_path=r"C:\Users\aDonovan\Testing123\Tests"#substitute your own path

    weights = [0.0,0.001,-0.1,1.0]#bias,size,days since mod,extension score

    files = scan_directory(root_path)
    analyzed = analyze_files(files)
    scored = score(analyzed,weights)

    #report
    output_csv = "automation_candidates.csv"
    write_csv_report(scored,output_csv)
    print(f"report printed")

if __name__ == "__main__":
    run()    