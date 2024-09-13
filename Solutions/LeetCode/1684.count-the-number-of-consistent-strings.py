#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        bit_mask = 0 # ?: All zeros?
        result = len(words)

        for character in allowed:
            bit = 1 << ord(character)-97
            bit_mask = bit_mask | bit
        for word in words:
            for character in word:
                bit = 1 << ord(character)-97

                if bit & bit_mask == 0:
                    result -= 1

                    break

        return result
# @lc code=end

