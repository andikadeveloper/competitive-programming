class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        truncate = ""
        word_count = 1
        
        for word in s:
            if word == " ":
                word_count += 1
            
            if word_count > k:
                break
            
            truncate += word
                
        return truncate

solution = Solution()
actual = solution.truncateSentence("chopper is not a tanuki", 5)
print(actual)
print(actual == "chopper is not a tanuki")