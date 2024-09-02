#
# @lc app=leetcode id=1894 lang=python3
#
# [1894] Find the Student that Will Replace the Chalk
#

# @lc code=start
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        last_chalks = k%sum(chalk) # ?: Reducing memory by combining variables?

        for i, c in enumerate(chalk):
            if last_chalks-c < 0:
                return i
            else:
                last_chalks -= c
        
# @lc code=end

