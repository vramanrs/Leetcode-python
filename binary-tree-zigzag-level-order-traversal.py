# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        q = deque()
        ans = []
        if root == None:
            return ans
        q.append(root)
        rev = False
        while q:
            temp = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                temp.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            if rev == True:
                temp.reverse()
            ans.append(temp)
            rev = not rev
        return ans




