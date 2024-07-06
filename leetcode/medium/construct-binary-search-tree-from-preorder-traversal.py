from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertToBst(self, arr: List[int]):
        if len(arr) == 0:
            return None
        if len(arr) == 1:
            return TreeNode(arr[0])
        
        l = []
        h = []
        
        for i in range(1, len(arr)):
            if arr[i] <= arr[0]:
                l.append(arr[i])
            else:
                h.append(arr[i])
        
        r = TreeNode(arr[0], self.convertToBst(l), self.convertToBst(h))
        
        return r
    
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.convertToBst(preorder)
    
solution = Solution()
actual = solution.bstFromPreorder([8,5,1,7,10,12])
print(actual)
print(actual.val == 8 and actual.left.val == 5 and actual.right.val == 10)
