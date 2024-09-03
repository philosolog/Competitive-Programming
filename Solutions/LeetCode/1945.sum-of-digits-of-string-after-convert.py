#
# @lc app=leetcode id=1945 lang=python3
#
# [1945] Sum of Digits of String After Convert
#

# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        from collections import Counter

        total = 0
        test_total = 0
        precomputed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8]
        frequency = Counter(s)
        
        for v in frequency.keys():
            total += (precomputed[ord(v)-97])*frequency[v]
        for _ in range(k-1):
            for d in str(total):
                test_total += int(d)
            
            total = test_total
            test_total = 0

        return total
    
# TODO: Optimize the space complexity

# @lc code=end

