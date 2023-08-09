class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    def check_symmetry(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and check_symmetry(left.left, right.right) and check_symmetry(left.right, right.left)
    
    if not root:
        return True
    return check_symmetry(root.left, root.right)

# Construct symmetric and asymmetric trees
symmetric_root = TreeNode(1)
symmetric_root.left = TreeNode(2)
symmetric_root.right = TreeNode(2)
symmetric_root.left.left = TreeNode(3)
symmetric_root.left.right = TreeNode(4)
symmetric_root.right.left = TreeNode(4)
symmetric_root.right.right = TreeNode(3)

asymmetric_root = TreeNode(1)
asymmetric_root.left = TreeNode(2)
asymmetric_root.right = TreeNode(2)
asymmetric_root.left.right = TreeNode(3)
asymmetric_root.right.right = TreeNode(3)

print("Is the symmetric tree symmetric?", is_symmetric(symmetric_root))  # Output should be True
print("Is the asymmetric tree symmetric?", is_symmetric(asymmetric_root))  # Output should be False
