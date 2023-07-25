## Repeated word
# challenge 31

## [Code](hashmap-repeated-word.py)
## [tests](../tests/test_hash_map.py)

 ## Approach and effiency:
Write a function called repeated word that finds the first word to occur more than once in a string
Arguments: string
Return: string
We tried to keep our code as simple as possible to the best performance by reducing space/Time complexity
so we end with the following:

### Big(O):
- Space complexity: O(1) 
- Time complexity: O(n)


## Solution
```
import re

def tokenize_string(input_string):
    words = re.findall(r'\b\w+\b', input_string.lower())
    return words


def count_word_frequency(word_list):
    word_freq = {}
    for word in word_list:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq


def find_first_repeated_word(word_list, word_freq):
   
    for word in word_list:
        if word_freq[word] > 1:
            return word
    return None


def repeated_word(input_string):
    
    words = tokenize_string(input_string)
    print("Tokenized words:", words)

 
    word_freq = count_word_frequency(words)
    print("Word frequency:", word_freq)

    
    repeated_word = find_first_repeated_word(words, word_freq)
    print("First repeated word:", repeated_word)

    return repeated_word



input_string = "This is a test string with a repeated word. Test it."
result = repeated_word(input_string)
print("Result:", result)

```

