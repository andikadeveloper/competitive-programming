class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) % 2 != 0:
            return False
        
        op = ["(", "[", "{"]
        x = {
            "(": 1,
            ")": 1,
            "[": 2,
            "]": 2,
            "{": 3,
            "}": 3
        }
        
        stack = []
        
        for l in s:
            if l in op:
                stack.append(l)
                continue
            
            if not stack:
                return False
            
            if x[l] != x[stack[-1]]:
                return False
                
            stack.pop()
                
        if stack:
            return False
        
        return True
    
solution = Solution()

print(solution.isValid("){"))