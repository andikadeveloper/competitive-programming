from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getTreeNode(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) < 1:
            return None
        
        if len(nums) < 2:
            return TreeNode(nums[0])
        
        largest = 0
        last = len(nums) - 1
        
        for i in range(len(nums)):
            if i > last:
                break
            
            if nums[i] > nums[largest]:
                largest = i
                
            if nums[last] > nums[largest]:
                largest = last
                
            last -= 1
                
        left = nums[0:largest]
        right = nums[largest + 1:]
        
        return TreeNode(nums[largest], self.getTreeNode(left), self.getTreeNode(right))
                
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.getTreeNode(nums)
    
solution = Solution()
actual = solution.constructMaximumBinaryTree([3,2,1,6,0,5])
print(actual.val)
print(actual.val == 6)
