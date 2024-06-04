strs = ["cir","car"]

def get_longest_word(strs):
    length = 0
    longest_word = ""
    for str in strs:
        if len(str) > length:
            length = len(str)
            longest_word = str
            
    return longest_word

def get_common_word(longest_word, strs):
    common_word = ""
    for i in range(len(longest_word)):
        letter = longest_word[i]
        count = 0
        
        for str in strs:
            if len(str) <= i or letter != str[i]:
                return common_word
            
            count +=1
        
        # When the letter for all the word is same
        if count == len(strs):
            common_word += letter
            
    return common_word

longest_word = get_longest_word(strs)
strs.remove(longest_word)

common_word = get_common_word(longest_word, strs)
        
print(common_word)