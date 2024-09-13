#
# @lc app=leetcode id=1310 lang=python3
#
# [1310] XOR Queries of a Subarray
#

# @lc code=start
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixes = [arr[0]]
        output = []

        for i, v in enumerate(arr):
            if i != 0:
                prefixes.append(prefixes[i-1]^v)

        for [x, y] in queries:
            if x != 0:
                output.append(prefixes[x-1]^prefixes[y])
            else:
                output.append(prefixes[y])
        
        return output  
# @lc code=end

