#
# @lc app=leetcode id=2028 lang=python3
#
# [2028] Find Missing Observations
#

# @lc code=start
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        new_sum = mean*(len(rolls)+n)-sum(rolls)

        if new_sum//n < 1 or new_sum//n + (new_sum%n != 0) > 6:
            return []
	
        # Note: Removable else operator!

        answer = [new_sum//n for _ in range(n)]

        for i in range(new_sum%n):
            answer[i] += 1

        return answer
# @lc code=end

