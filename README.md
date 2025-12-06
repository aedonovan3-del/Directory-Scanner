# Directory-Scanner
Directory scanner that identifies potential candiates for workflow automation by producing a csv file of files within the directory and uses a very rudimentary perceptron calculation and assigned numerical values to files extension type to create a ranked list of files that could potentially benefit from workflow automation

This package is extremely rudimentary with the goal of being as minimal as possible while creating scaffolding for a more robust scoring sytem in the future

Contains:

1. scanner : using os.walk() and os.stat() to extract metadata to include file path, file name, size (kb), and last modified date
2. analyzer : manually maps priority values to related keys (file extension types) and convert the metadata to the feature vector using manual weights assigned in the run module
3. scorer  : uses a rudimentary perceptron to weight the files and assign a score
4. report : writes the ranked file metadata with score to a report labelled automation_candidates.csv to the directory where the modules are stored
5. run : runs the modules, to implement, include the relevent path in the module to test (py run.py)


