#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
	def isPalindrome(self, s: str) -> bool:
		valid = [c.lower() for c in s if c.isalnum()]
		
		return valid == valid[::-1]
# @lc code=end

