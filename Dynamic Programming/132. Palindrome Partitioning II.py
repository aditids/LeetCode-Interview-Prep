# 132. Palindrome Partitioning II

class Solution:
    def minCut(self, s: str) -> int:
        # Base case if given string is a palindrome
        if s==s[::-1]:
            return 0

        n = len(s)
        # For one cut
        for i in range(n):
            if s[:i]==s[:1][::-1] and s[i:]==s[i:][::-1]:
                return 1

        dp = [0]*n
        isPalindrome = [[False]*n for i in range(n)]
        for j in range(n):
            count = j
            for i in range(j+1):
                if s[i]==s[j] and (j-i<=1 or isPalindrome[i+1][j-1]):
                    isPalindrome[i][j] = True
                    if i==0:
                        count = 0
                    else:
                        count = min(count,dp[i-1]+1)
            dp[j] = count
        return dp[-1]