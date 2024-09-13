#
# @lc app=leetcode id=1310 lang=python3
#
# [1310] XOR Queries of a Subarray
#

# @lc code=start
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        output = []

        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1] # Note: Originally did NOT utilize the input array. Do note that this method changes the input array, so it is not recommended though an optimization.
        for [x, y] in queries:
            if x != 0:
                output.append(arr[x-1]^arr[y])
            else:
                output.append(arr[y])
        
        return output  
# @lc code=end

