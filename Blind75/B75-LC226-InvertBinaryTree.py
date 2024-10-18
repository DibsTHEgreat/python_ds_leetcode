# Leetcode 226: Invert Binary Tree
# Problem List: Blind 75
# Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree, Recursion

# Time Complexity: 
# Space Complexity: 

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the root is None, there's nothing to invert, so return None
        if not root:
            return None
        
        # Swap the left and right children of the current node
        temp = root.left
        root.left = root.right
        root.right = temp
        
        # Recursively invert the left subtree
        self.invertTree(root.left)
        # Recursively invert the right subtree
        self.invertTree(root.right)
        
        # Return the root of the inverted tree
        return root