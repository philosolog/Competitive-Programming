#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        if set(s1.split()) == set(s2.split()):
            return []
            
        return [v for v, c in Counter((s1+" "+s2).split()).items() if c == 1]

# ?: Consider the set optimization.
# @lc code=end

