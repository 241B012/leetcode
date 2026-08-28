# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int):
        
        def build(start, end):
            if start > end:
                return [None]

            result = []

            # Try every value as the root
            for root_val in range(start, end + 1):

                # Generate all possible left subtrees
                left_trees = build(start, root_val - 1)

                # Generate all possible right subtrees
                right_trees = build(root_val + 1, end)

                # Combine every left subtree with every right subtree
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        result.append(root)

            return result

        return build(1, n)