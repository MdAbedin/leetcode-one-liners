class Solution:
    def longestPalindrome(self, s: str) -> str:
        return max((ss for i1 in range(len(s)) for i2 in range(i1,len(s)) if (ss := s[i1:i2+1]) == ss[::-1]),key=len)
