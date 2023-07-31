from hashtable import HashTable

def hashmap_left_join(table1: HashTable, table2: HashTable):
    """
    Function to left join two hashmaps.

    Returns:
        List of lists containing the key, value from table1, and value from table2.
    """
    arr = []
    for key in table1.keys():
        arr.append([key, table1.get(key), table2.get(key)])
    return arr