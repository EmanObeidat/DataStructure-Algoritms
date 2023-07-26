class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_intersection(tree1, tree2):
    def traverse_and_build_map(node, value_map):
        if node is None:
            return
        value_map[node.value] = True
        traverse_and_build_map(node.left, value_map)
        traverse_and_build_map(node.right, value_map)

    def find_common_values(node, value_map, result_set):
        if node is None:
            return
        if node.value in value_map:
            result_set.add(node.value)
        find_common_values(node.left, value_map, result_set)
        find_common_values(node.right, value_map, result_set)


    value_map = {}
    traverse_and_build_map(tree1, value_map)
    result_set = set()
    find_common_values(tree2, value_map, result_set)
    return result_set

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


result = tree_intersection(tree1, tree2)
print("Common values in the two trees:", result)