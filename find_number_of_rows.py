import csv

def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    list=data.split('\n')
    #list1=list[0].split(',')

    return (len(list)-1)
f=open('data.csv').read()
print(find_number_of_rows(f))


# Read the csv file
