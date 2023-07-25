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
