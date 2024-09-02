class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return max(([seen := set(), len(list(takewhile(lambda i: [s[i] not in seen,seen.add(s[i])][0], range(i,len(s)))))][1] for i in range(len(s))),default=0)
