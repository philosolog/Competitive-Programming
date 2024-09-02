#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapping = dict()
        
        for i in range(len(numbers)):
            if target - numbers[i] not in mapping:
                mapping[target - numbers[i]] = i
        for k, v in mapping.items():
            if k in numbers:
                return [v+1, numbers.index(k, v+1)+1]
            
# TODO: Opptimize
# @lc code=end

