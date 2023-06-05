def validate_brackets(string):
    stack = []  # Stack to store opening brackets

    # Define the mapping of opening brackets to closing brackets
    brackets_map = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    # Iterate through each character in the string
    for char in string:
        # If the character is an opening bracket, push it onto the stack
        if char in brackets_map.keys():
            stack.append(char)
        # If the character is a closing bracket
        elif char in brackets_map.values():
            # Check if the stack is empty or the top of the stack doesn't match the closing bracket
            if not stack or char != brackets_map[stack.pop()]:
                return False

    # If there are any remaining opening brackets in the stack, return False
    if stack:
        return False

    # If all brackets are balanced, return True
    return True
string1 = "(([{()}]))"
print(validate_brackets(string1))  # Output: True

string2 = "{[}]"
print(validate_brackets(string2))  # Output: False
string3="[({})]"
print(validate_brackets(string3)) #True
string4="[([{])]"
print(validate_brackets(string4)) #false