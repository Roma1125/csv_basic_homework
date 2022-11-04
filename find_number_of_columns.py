import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    return len(list(data)[0])
f=open('data.csv')
r=csv.reader(f)
print(find_number_of_columns(r))

# Read the csv file