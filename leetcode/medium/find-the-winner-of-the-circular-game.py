class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + k) % i
        return ans + 1
    
solution = Solution()
actual = solution.findTheWinner(6, 5)
print(actual)
print(actual == 1)
