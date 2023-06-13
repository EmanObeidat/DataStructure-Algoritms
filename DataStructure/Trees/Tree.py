class Node:
    '''
    Create a Node class with properties for the value stored in the node, the left child node, and the right child node.
    '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    ''' 
    The BinaryTree class should have an __init__ method that initializes the root node to None.
    Implement three traversal methods: preorder_traversal(), inorder_traversal(), and postorder_traversal().
    '''
    def __init__(self):
        self.root = None

    def preorder_traversal(self, node, result):
         '''
         If the node is not None:
            Append the node value to result.
            Recursively call _preorder_traversal_recursive() on the left child of the node.
            Recursively call _preorder_traversal_recursive() on the right child of the node.
            Return result.
         '''
         if node is not None:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

    def inorder_traversal(self, node, result):
        '''
        If the node is not None:
        Recursively call _inorder_traversal_recursive() on the left child of the node.
        Append the node value to result.
        Recursively call _inorder_traversal_recursive() on the right child of the node.
        Return result
        '''
        if node is not None:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)

    def postorder_traversal(self, node, result):
        if node is not None:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)
    def find_maximum_value(self):
        if self.root is None:
            return None
        
        def max_value_recursive(node):
            if node is None:
                return float('-inf')
            
            left_max = max_value_recursive(node.left)
            right_max = max_value_recursive(node.right)
            
            return max(node.value, left_max, right_max)
        
        return max_value_recursive(self.root)

class BinarySearchTree(BinaryTree):

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_helper(self.root, value)

    def _add_helper(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_helper(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_helper(node.right, value)

    def contains(self, value):
        return self._contains_helper(self.root, value)

    def _contains_helper(self, node, value):
        if node is None:
            return False
        elif value == node.value:
            return True
        elif value < node.value:
            return self._contains_helper(node.left, value)
        else:
            return self._contains_helper(node.right, value)
    

    








# Creating a binary tree
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Perform depth-first traversals
preorder_result = []
tree.preorder_traversal(tree.root, preorder_result)
print("Preorder traversal:", preorder_result)  # Output: [1, 2, 4, 5, 3]

inorder_result = []
tree.inorder_traversal(tree.root, inorder_result)
print("Inorder traversal:", inorder_result)  # Output: [4, 2, 5, 1, 3]

postorder_result = []
tree.postorder_traversal(tree.root, postorder_result)
print("Postorder traversal:", postorder_result)  # Output: [4, 5, 2, 3, 1]

# Creating a binary search tree
bst = BinarySearchTree()
bst.add(10)
bst.add(5)
bst.add(15)
bst.add(2)
bst.add(7)
bst.add(12)
bst.add(20)

# Check if values are present in the BST
print("Contains 7:", bst.contains(7))  # Output: True
print("Contains 8:", bst.contains(8))  # Output: False
binary_tree = BinaryTree()
# Assume the binary tree is populated with values

maximum_value = bst.find_maximum_value()
print("The maximum value in the binary tree is:", maximum_value)
