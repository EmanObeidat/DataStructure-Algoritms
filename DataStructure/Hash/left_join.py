from Hash.hashtable import HashTable
def hashmap_left_join(T1: HashTable, T2: HashTable):
    """
    Function to left join two hashmaps.

    Returns:
        Hashtable: Hashtable containing the left join result with keys from table1 and values from both tables.
    """
    result = HashTable()
    for key in T1.keys():
        value1 = T1.get(key)
        value2 = T2.get(key)
        result.set(key, [value1, value2])
    return result