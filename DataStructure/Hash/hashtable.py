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
        return False

    def keys(self):
        keys = []
        for bucket in self.table:
            for pair in bucket:
                keys.append(pair[0])
        return list(set(keys))  


ht = HashTable()

ht.set("name", "John")
ht.set("age", 30)
ht.set("city", "New York")

print(ht.get("name")) 
print(ht.get("age"))   
print(ht.get("gender"))  

print(ht.has("city"))  
print(ht.has("gender"))  

print(ht.keys()) 

ht.set("dog", "Buddy")
ht.set("god", "Friend")
ht.set("dgo", "Pal")

print(ht.get("dog"))  
print(ht.get("god"))  
print(ht.get("dgo"))  


print(ht._hash("name"))  
print(ht._hash("city")) 