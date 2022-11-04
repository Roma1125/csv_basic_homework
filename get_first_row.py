#Define function,Get coloumn names from a csv file
import csv
def get_first_row(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    list=data.split('\n')
    list1=list[0].split(',')

    return ((list1))
f=open('data.csv').read()
print(get_first_row(f))

    
# Read the csv file