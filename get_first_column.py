def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    d=[]
    list=data.split('\n')
    for i in range(len(list)):
        if list[i]!='':

            d.append((list[i].split(','))[0])
    
  
    return ((d))
f=open('data.csv').read()
print(get_first_column(f))
    
# Read the csv file