import unittest
from hashtable import HashTable

class TestHashTable(unittest.TestCase):
    def test_set_and_get(self):
        ht = HashTable()
        ht.set("name", "John")
        ht.set("age", 30)
        ht.set("city", "New York")

        self.assertEqual(ht.get("name"), "John")
        self.assertEqual(ht.get("age"), 30)
        self.assertIsNone(ht.get("gender"))

    def test_keys(self):
        ht = HashTable()
        ht.set("name", "John")
        ht.set("age", 30)
        ht.set("city", "New York")

        keys = ht.keys()
        self.assertCountEqual(keys, ["name", "age", "city"])

    def test_collision(self):
        ht = HashTable()
        ht.set("dog", "Buddy")
        ht.set("god", "Friend")
        ht.set("dgo", "Pal")

        self.assertEqual(ht.get("dog"), "Buddy")
        self.assertEqual(ht.get("god"), "Friend")
        self.assertEqual(ht.get("dgo"), "Pal")

    def test_hash_range(self):
        ht = HashTable()
        hash_val = ht._hash("name")
        self.assertTrue(0 <= hash_val < ht.size)

    def test_has(self):
        ht = HashTable()
        ht.set("name", "John")
        ht.set("age", 30)

        self.assertTrue(ht.has("name"))
        self.assertTrue(ht.has("age"))
        self.assertFalse(ht.has("city"))

if __name__ == "__main__":
    unittest.main()
