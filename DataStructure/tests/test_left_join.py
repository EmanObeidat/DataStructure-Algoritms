from hashtable import HashTable
import pytest
from left_join import hashmap_left_join
def test_hashmap_left_join():
   
    table1 = HashTable()
    table2 = HashTable()

    table1.put("happy", "joyful")
    table1.put("sad", "unhappy")
    table1.put("hot", "warm")
    table1.put("cold", "chilly")

    table2.put("happy", "sad")
    table2.put("hot", "cold")
    table2.put("rich", "poor")

    result = hashmap_left_join(table1, table2)
    assert result == [
        ["happy", "joyful", "sad"],
        ["sad", "unhappy", None],
        ["hot", "warm", "cold"],
        ["cold", "chilly", None]
    ]

def test_hashmap_left_join_empty_tables():
    table1 = HashTable()
    table2 = HashTable()

    result = hashmap_left_join(table1, table2)

    assert result == []

def test_hashmap_left_join_missing_keys():
    table1 = HashTable()
    table2 = HashTable()

    table1.put("happy", "joyful")
    table1.put("sad", "unhappy")
    table2.put("happy", "sad")
    table2.put("rich", "poor")

    result = hashmap_left_join(table1, table2)

    assert result == [
        ["happy", "joyful", "sad"],
        ["sad", "unhappy", None]
    ]

