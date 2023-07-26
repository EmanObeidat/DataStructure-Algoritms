import pytest
from Trees.tree_intersection import tree_intersection,TreeNode



def test_tree_intersection():
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)
    tree1.left.right = TreeNode(5)
    

    tree2 = TreeNode(2)
    tree2.left = TreeNode(3)
    tree2.right = TreeNode(6)
    tree2.left.left = TreeNode(4)
    tree2.left.right = TreeNode(7)
    result1 = tree_intersection(tree1, tree2)
    
    assert result1 == {2, 3, 4}