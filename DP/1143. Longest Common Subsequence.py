class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
                
        a = text1
        b = text2 

        N = len(a)
        M = len(b)

        dp = [[0]*(M+1) for _ in range(N+1)]

        for i in range(1, N+1):
            for j in range(1, M+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[N][M]
        
