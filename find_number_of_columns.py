import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    list=data.split('\n')
    list1=list[0].split(',')

    return (len(list1))
f=open('data.csv').read()
print(find_number_of_columns(f))

# Read the csv file