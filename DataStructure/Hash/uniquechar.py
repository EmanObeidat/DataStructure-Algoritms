from hashtable import HashTable

def has_unique_characters(str):
    lower_str=str.lower ()
    char_list=[char for char in lower_str]
    table=HashTable()
    for char in char_list:
         if table.has(char):
             return "False"
         table.set(char,char)
    return "True"

print(has_unique_characters("abc defg")) 
print(has_unique_characters("Hello"))     
print(has_unique_characters("WorlD"))     
print(has_unique_characters("world"))    
