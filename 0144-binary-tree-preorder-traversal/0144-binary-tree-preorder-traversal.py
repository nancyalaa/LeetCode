# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        stack = [root]
        while stack:
            curr_node = stack.pop()
            if curr_node:
                answer.append(curr_node.val)
                stack.append(curr_node.right)
                stack.append(curr_node.left)        
        return answer