from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertToArray(self, t: TreeNode) -> List[int]:
        if t is None:
            return []
        
        if t.left is None and t.right is None:
            return [t.val]
        
        return self.convertToArray(t.left) + [t.val] + self.convertToArray(t.right)
    
    def convertToTree(self, arr: List[int], i: int, n: int):
        root = None
        
        if i <= n:
            mid = (i + n) // 2
            root = TreeNode(arr[mid])
            root.left = self.convertToTree(arr, i, mid-1)
            root.right = self.convertToTree(arr, mid+1, n)
        
        return root
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = self.convertToArray(root)
        
        return self.convertToTree(arr, 0, len(arr) - 1)
    
solution = Solution()
actual = solution.balanceBST(TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4)))))
print(actual.val)
print(actual.val == 2)
