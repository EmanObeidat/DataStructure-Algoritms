class Node: #class for creating a node 
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack: 
    def __init__(self):
        self.top = None
# push node into the top of stack
    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
# pop the top node
    def pop(self):
        if not self.top:
            raise Exception("Stack is empty!!")
        value = self.top.value
        self.top = self.top.next
        return value
# return the top
    def peek(self):
        if not self.top:
            raise Exception("Stack is empty!!")
        return self.top.value
# check if the stack is empty or not 
    def is_empty(self):
        return not bool(self.top)   
def validate_brackets(string):
    stack = Stack()
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in string:
        if char in bracket_pairs.keys():
            stack.push(char)
        elif char in bracket_pairs.values():
            if stack.is_empty() or bracket_pairs[stack.pop()] != char:
                return False
    return stack.is_empty()
string1 = "(([{()}]))"
print(validate_brackets(string1))  # Output: True

string2 = "{[}]"
print(validate_brackets(string2))  # Output: False
string3="[({})]"
print(validate_brackets(string3)) #True
string4="[([{])]"
print(validate_brackets(string4)) #false