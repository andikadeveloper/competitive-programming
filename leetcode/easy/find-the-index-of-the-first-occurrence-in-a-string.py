class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            h = haystack[i]
            last_index = len(haystack)
            
            if h != needle[0] or len(needle) > last_index - i:
                continue
            
            count = 0
            for j in range(len(needle)):
                if haystack[i + j] == needle[j]:
                    count += 1
                    
            if count == len(needle):
                return i
        
        return -1

solution = Solution()

print(solution.strStr("a", "a"))