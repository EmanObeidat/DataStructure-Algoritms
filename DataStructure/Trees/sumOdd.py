class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def sum_odd_numbers(root):
    """
    Calculates the sum of all the odd numbers in a binary search tree.

    Args:
        root (TreeNode): The root node of the binary search tree.

    Returns:
        int: The sum of all the odd numbers in the binary search tree.
    """
    if root is None:
        return 0

    stack = []
    current = root
    total_sum = 0

    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            if current.val % 2 != 0:
                total_sum += current.val
            current = current.right
        else:
            break

    return total_sum
# Create a binary search tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Calculate the sum of odd numbers in the BST
result = sum_odd_numbers(root)
print("Sum of odd numbers:", result)
