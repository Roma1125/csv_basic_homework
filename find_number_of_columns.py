import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    d=csv.reader(data)
    return len(list(d)[0])
f=open('data.csv')
print(find_number_of_columns(f))

# Read the csv file