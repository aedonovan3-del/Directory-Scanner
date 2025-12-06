#Scorer

def perceptron_activation(x,weights):
    """
    Purpose: isolate a scoring method for file meta data to sort for possible workflow automation candidates
    Parameters: mapped attributes, weights, biases
    Returns: bias + attribute weights
    """

    x_with_bias = [1] + list(x)
    activation = 0
    for w,xi in zip(weights,x_with_bias):
        activation += w*xi
    return activation    

def score(file_attributes,weights):
    """
    Purpose: scores and ranks the files
    Parameters: the attribute dictionaries (path, name, size, date, etc...)
    Returns: updates the dictionaries with the scores
    """
    scored_files=[]

    for record in file_attributes:
        x = record["Attributes"]
        skore = perceptron_activation(x,weights)

        new_record = dict(record)
        new_record["Score"] = skore
        scored_files.append(new_record)

    def get_score(record):
        return record["Score"]

    scored_files.sort(key=get_score,reverse=True)
    return scored_files