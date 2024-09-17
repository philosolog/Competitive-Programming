#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#

# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(set(timePoints)) != len(timePoints):
            return 0

        m = float("inf")
        timePoints = set(timePoints)
        timePoints = [60*int(s[:2]) + int(s[3:]) for s in timePoints]
        timePoints.sort()

        for i in range(0, len(timePoints)-1):
            m = min(m, timePoints[i+1]-timePoints[i])

        return min(m, 1440-timePoints[-1]+timePoints[0])

# TODO: Consider the trivial optimizations
# @lc code=end

