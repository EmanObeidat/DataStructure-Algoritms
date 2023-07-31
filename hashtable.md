
# Hash table


## [Code](./DataStructure/Hash/hashtable.py)
## [tests](./DataStructure/tests/test_hashtable.py)

## Approach & Efficiency

```Implement a Hashtable Class with the following methods:set, get ,contains, keys, hash```
```The hash table is instantiated with 1024 buckets that have a default value of None.```
```Collisions are handled with the linked list data structure.```


### Big O:
the following table will show Big(O) for each method

| **Method** | **Time** | **Space** |
|------------|----------|-----------|
| hash       | O(1)     | O(1)      |
| set        | O(1)     | O(1)      |
| get        | O(n)     | O(n)      |
| has    | O(n)     | O(n)      |
| keys        | O(n)     | O(n)      |

## Solution 
```
class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def has(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return True
```
### This code do the next functionality:
```
1. Setting a key/value to your hashtable results in the value being in the data structure
2. Retrieving based on a key returns the value stored
3. Successfully returns null for a key that does not exist in the hashtable
4. Successfully returns a list of all unique keys that exist in the hashtable
5. Successfully handle a collision within the hashtable
6. Successfully retrieve a value from a bucket within the hashtable that has a collision
7. Successfully hash a key to an in-range value
```