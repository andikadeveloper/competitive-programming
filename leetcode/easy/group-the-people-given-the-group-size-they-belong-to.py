from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupPeoples = {}
        
        for i in range(len(groupSizes)):
            group = groupSizes[i]
            
            if group in groupPeoples:
                groupPeoples[group] = groupPeoples[group] + [i]
            else:
                groupPeoples[group] = [i]
                
        result = []
        
        for group, peoples in groupPeoples.items():
            if group == len(peoples):
                result.append(peoples)
            else:
                count = 0
                for i in range(group, len(peoples) + 1, group):
                    result.append(peoples[count:i])
                    count = i
                
        return result
    
solution = Solution()
actual = solution.groupThePeople([3,3,3,3,3,1,3])
print(actual)
print(actual == [[5],[0,1,2],[3,4,6]])